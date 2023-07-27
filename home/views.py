from django.views.generic import View
from django.shortcuts import render

from .forms import FormSearchReceipt

from .helper import HelperHome

class HomeView(View):
    def get(self, request, *args, **kwarg):
        form = FormSearchReceipt()
        sales_today, total_count, total_sale = HelperHome.sales_today()
        context = {
            'form' : form,
            'sales_today' : sales_today,
            'total_count' : total_count,
            'total_sale' : total_sale
        }
        return render(request, 'home.html', context)
    
    def post(self, request, *args, **kwarg):
        form = FormSearchReceipt(request.POST)
        if not form.is_valid():
            sales_today, total_sale = HelperHome.sales_today()
            context = {
            'form' : form,
            'sales_today' : sales_today,
            'total_sale' : total_sale
            }
            return render(request, 'home.html', context)
        
        receipt_all = HelperHome.get_receipt(form)
        context = {
            'form' : form,
            'receipts' : receipt_all,
        }
        return render(request, 'detail_receipt.html', context)