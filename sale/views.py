from django.shortcuts import render
from django.views.generic import View
# Create your views here.

class SaleListView(View):
    def get(self, request, *arg, **kwarg):
        context = {
            
        }
        return render(request, 'sale/sale_list.html', context, status=200)