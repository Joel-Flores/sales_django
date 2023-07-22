from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View

from src.helper import HelperApp
from .forms import FormClient

# Create your views here.
class PayOrder(View):
    def get(self, request, *args, **kwarg):
        form = FormClient()
        orders = HelperApp.get_order(request)
        orders = False if len(orders) == 0 else orders
        total = HelperApp.get_total(request) if orders else None
        context = {
            'form' : form,
            'orders' : orders,
            'total' : total
        }
        return render(request, 'receipts/view_orders.html', context, )
    
    def post(self, request, *args, **kwarg):
        form = FormClient(request.POST)
        if not form.is_valid():
            orders = HelperApp.get_order(request)
            orders = False if len(orders) == 0 else orders
            total = HelperApp.get_total(request) if orders else None
            context = {
                'form' : form,
                'orders' : orders,
                'total' : total
            }
            return render(request, 'receipts/view_orders.html', context, )
        
        
        return redirect('home')