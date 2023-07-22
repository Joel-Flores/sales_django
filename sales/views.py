from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View

from .helper import HelperSale
from src.helper import HelperApp
from product.helper import HelperProduct
from .forms import form_add_cart_to_products

# Create your views here.
class AddCartFood(View):
    def get(self, request, *args, **kwarg):
        products = HelperProduct.get_products_filter_type(1)
        form = form_add_cart_to_products(products)
        context = {
            'products' : products,
            'form' : form
        }
        return render(request, 'sales/addtocart.html', context, )
    
    def post(self, request, *args, **kwarg):
        products = HelperProduct.get_products_filter_type(1)
        form = form_add_cart_to_products(products,request.POST)
        if form.is_valid():
            orders = HelperApp.get_order(request)
            for product_name, count in form.data.items():
                if count is None or count == 0:
                    continue
            
                product_data = HelperSale.search_in_list(product_name, products)
                if product_data is None:
                    continue
                
                order = HelperSale.search_in_list(product_name, orders)
                if order is None:
                    # Si no existe, agregamos un nuevo diccionario de orden
                    orders.append(HelperApp.new_order(product_data, count))
                    
                else:
                    # Si la orden ya existe, sumamos el contador
                    HelperApp.update_order(order, product_data, count)
                    
            HelperApp.update_order_in_session(request, orders)
            return redirect('home')
        context = {
            'products' : products,
            'form' : form
        }
        return render(request, 'sales/addtocart.html', context, )

class AddCartSoda(View):
    def get(self, request, *args, **kwarg):
        products = HelperProduct.get_products_filter_type(2)
        form = form_add_cart_to_products(products)
        context = {
            'products' : products,
            'form' : form
        }
        return render(request, 'sales/addtocart.html', context, )
    
    def post(self, request, *args, **kwarg):
        products = HelperProduct.get_products_filter_type(2)
        form = form_add_cart_to_products(products,request.POST)
        if form.is_valid():
            orders = HelperApp.get_order(request)
            for product_name, count in form.data.items():
                if count is None or count == 0:
                    continue
            
                product_data = HelperSale.search_in_list(product_name, products)
                if product_data is None:
                    continue
                
                order = HelperSale.search_in_list(product_name, orders)
                if order is None:
                    # Si no existe, agregamos un nuevo diccionario de orden
                    orders.append(HelperApp.new_order(product_data, count))
                    
                else:
                    # Si la orden ya existe, sumamos el contador
                    HelperApp.update_order(order, product_data, count)
                    
            HelperApp.update_order_in_session(request, orders)
            return redirect('home')
        context = {
            'products' : products,
            'form' : form
        }
        return render(request, 'sales/addtocart.html', context, )

class DeteleOrder(View):
    def get(self, request, *args, **kwarg):
        context = {
            
        }
        return render(request, '.html', context, )

class ClearCart(View):
    def get(self, request, *args, **kwarg):
        context = {
            
        }
        return render(request, '.html', context, )

