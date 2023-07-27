from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.views import View

from .helper import HelperSale
from src.helper import HelperApp
from product.helper import HelperProduct
from .forms import form_add_cart_to_products

# Create your views here.
class AddCart(View):
    def get(self, request, *args, **kwarg):
        id = self.kwargs['pk']
        products = HelperProduct.get_products_filter_type(id)
        form = form_add_cart_to_products(products)
        context = {
            'products' : products,
            'form' : form
        }
        return render(request, 'sales/addtocart.html', context, )
    
    def post(self, request, *args, **kwarg):
        id = self.kwargs['pk']
        products = HelperProduct.get_products_filter_type(id)
        form = form_add_cart_to_products(products,request.POST)
        if not form.is_valid():
            context = {
                'products' : products,
                'form' : form
            }
            return render(request, 'sales/addtocart.html', context, )
        
        orders = HelperApp.get_order(request)
        for product_name, count in form.data.items():
            try:
                if int(count) == 0:
                    continue
            except ValueError:
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
        messages.success(request, 'Producto/s  agregados al carrito')
        return redirect('home:home')

class DeteleOrder(View):
    def get(self, request, *args, **kwarg):
        id = self.kwargs['pk']
        orders = HelperApp.get_order(request)
        orders = [order for order in orders if order["id"] != id]
        HelperApp.update_order_in_session(request, orders)
        messages.success(request, 'Se elimino la orden')
        return redirect('receipts:pay')

class ClearCart(View):
    def get(self, request, *args, **kwarg):
        request.session.pop('orders')
        request.session.pop('total')
        messages.success(request, 'Carrito limpio')
        return redirect('home:home')

