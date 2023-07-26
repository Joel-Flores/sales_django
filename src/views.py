from django.views.generic import View
from django.shortcuts import render

from product.helper import HelperTypeProduct
class HomeView(View):
    def get(self, request, *args, **kwarg):
        type_products = HelperTypeProduct.get_type_products()
        context = {
            'type_products':type_products
        }
        return render(request, 'home.html', context)