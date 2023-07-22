from django.shortcuts import render
from django.views import View

# Create your views here.
class AddCartFood(View):
    def get(self, request, *args, **kwarg):
        context = {
            
        }
        return render(request, '.html', context, )
    
    def post(self, request, *args, **kwarg):
        context = {
            
        }
        return render(request, '.html', context, )

class AddCartSoda(View):
    def get(self, request, *args, **kwarg):
        context = {
            
        }
        return render(request, '.html', context, )
    
    def post(self, request, *args, **kwarg):
        context = {
            
        }
        return render(request, '.html', context, )

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

