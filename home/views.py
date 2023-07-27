from django.views.generic import View
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

from .forms import FormSearchReceipt
from .forms import CustomUserForm

from .helper import HelperHome

class RegisterView(View):
    def get(self, request, *args, **kwarg):
        form = CustomUserForm()
        context = {
            'form' : form
        }
        print(form)
        return render(request, 'registration/register.html', context)
    
    def post(self, request, *args, **kwarg):
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password1'])
            login(request, user)
            messages.success(request, 'usuario creado correctamente')
            return redirect('home:home')
        print(form.data)
        context = {
            'form' : form
        }
        return render(request, 'registration/register.html', context)

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
        return render(request, 'home/home.html', context)
    
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
        return render(request, 'hoem/detail_receipt.html', context)