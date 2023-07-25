from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from .models import ProductName
from .models import ProductType

from .forms import ProductNameForm
from .forms import ProductTypeForm

# Create your views here.

#CRUD product_type
class ProductTypeCreate(CreateView):
    model = ProductType
    form_class = ProductTypeForm
    template_name = 'table_product_type/product_type_form.html'
    success_url = reverse_lazy('product:product_type_read')

class ProductTypeRead(ListView):
    model = ProductType
    template_name = 'table_product_type/product_type_read.html'

class ProductTypeUpdate(UpdateView):
    model = ProductType
    form_class = ProductTypeForm
    template_name = 'table_product_type/product_type_form.html'
    success_url = reverse_lazy('product:product_type_read')

class ProductTypeDelete(DeleteView):
    model = ProductType
    template_name = 'table_product_type/product_type_delete.html'
    success_url = reverse_lazy('product:product_type_read')

#CRUD product_name
class ProductCreate(CreateView):
    model = ProductName
    form_class = ProductNameForm
    template_name = 'table_product_name/product_form.html'
    success_url = reverse_lazy('product:product_read')

class ProductRead(ListView):
    model = ProductName
    template_name = 'table_product_name/product_read.html'

class ProductUpdate(UpdateView):
    model = ProductName
    form_class = ProductNameForm
    template_name = 'name_product_name/product_form.html'
    success_url = reverse_lazy('product:product_read')

class ProductDelete(DeleteView):
    model = ProductName
    template_name = 'name_product_name/product_delete.html'
    success_url = reverse_lazy('product:product_read')