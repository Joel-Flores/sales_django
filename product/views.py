from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin

from .models import ProductName
from .models import ProductType

from .forms import ProductNameForm
from .forms import ProductTypeForm

# Create your views here.

#CRUD product_type
class ProductTypeCreate(UserPassesTestMixin, CreateView):
    model = ProductType
    form_class = ProductTypeForm
    template_name = 'product/table_product_type/product_type_form.html'
    success_url = reverse_lazy('product:product_type_read')
    
    def test_func(self):
        return self.request.user.is_staff

class ProductTypeRead(UserPassesTestMixin, ListView):
    model = ProductType
    template_name = 'product/table_product_type/product_type_read.html'
    
    def test_func(self):
        return self.request.user.is_staff

class ProductTypeUpdate(UserPassesTestMixin, UpdateView):
    model = ProductType
    form_class = ProductTypeForm
    template_name = 'product/table_product_type/product_type_form.html'
    success_url = reverse_lazy('product:product_type_read')
    
    def test_func(self):
        return self.request.user.is_staff

class ProductTypeDelete(UserPassesTestMixin, DeleteView):
    model = ProductType
    template_name = 'product/table_product_type/product_type_delete.html'
    success_url = reverse_lazy('product:product_type_read')
    
    def test_func(self):
        return self.request.user.is_staff

#CRUD product_name
class ProductCreate(UserPassesTestMixin, CreateView):
    model = ProductName
    form_class = ProductNameForm
    template_name = 'product/table_product_name/product_form.html'
    success_url = reverse_lazy('product:product_read')
    
    def test_func(self):
        return self.request.user.is_staff

class ProductRead(UserPassesTestMixin, ListView):
    model = ProductName
    template_name = 'product/table_product_name/product_read.html'
    
    def test_func(self):
        return self.request.user.is_staff

class ProductUpdate(UserPassesTestMixin, UpdateView):
    model = ProductName
    form_class = ProductNameForm
    template_name = 'product/table_product_name/product_form.html'
    success_url = reverse_lazy('product:product_read')
    
    def test_func(self):
        return self.request.user.is_staff

class ProductDelete(UserPassesTestMixin, DeleteView):
    model = ProductName
    template_name = 'product/table_product_name/product_delete.html'
    success_url = reverse_lazy('product:product_read')
    
    def test_func(self):
        return self.request.user.is_staff