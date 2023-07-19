from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from .models import ProductName
from .forms import ProductNameForm

# Create your views here.
class ProductCreate(CreateView):
    model = ProductName
    form_class = ProductNameForm
    template_name = 'sale/product_form.html'
    success_url = reverse_lazy('sale:read')
    
class ProductRead(ListView):
    model = ProductName
    template_name = 'sale/product_read.html'
    
class ProductUpdate(UpdateView):
    model = ProductName
    form_class = ProductNameForm
    template_name = 'sale/product_form.html'
    success_url = reverse_lazy('sale:read')

class ProductDelete(DeleteView):
    model = ProductName
    template_name = 'sale/product_delete.html'
    success_url = reverse_lazy('sale:read')