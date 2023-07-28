from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin

from django.views import View
from django.views.generic import ListView
from django.views.generic import DeleteView

from django.urls import reverse_lazy

from .forms import FormClient
from .forms import FormReceipt
from .forms import FormReceiptFilter

from .models import Receipts

from .helper import HelperClients
from .helper import HelperReceipts

from src.create_pdf import CreatePdf
from src.helper import HelperApp
from sales.helper import HelperSale

# Create your views here.
class PayOrder(View):
    def get(self, request, *args, **kwarg):
        form_client = FormClient()
        form_received = FormReceipt()
        orders = HelperApp.get_order(request)
        orders = False if len(orders) == 0 else orders
        total = HelperApp.get_total(request) if orders else None
        context = {
            'form_client' : form_client,
            'form_received' : form_received,
            'orders' : orders,
            'total' : total
        }
        return render(request, 'receipts/view_orders.html', context, )
    
    def post(self, request, *args, **kwarg):
        form_client = FormClient(request.POST)
        form_received = FormReceipt(request.POST)
        if not (form_client.is_valid() and form_received.is_valid()):
            orders = HelperApp.get_order(request)
            orders = False if len(orders) == 0 else orders
            total = HelperApp.get_total(request) if orders else None
            context = {
                'form_client' : form_client,
                'form_received' : form_received,
                'orders' : orders,
                'total' : total
            }
            return render(request, 'receipts/view_orders.html', context, )
        
        client = HelperClients.search_client(form_client)
        if HelperClients.check_pay(request, form_received):
            received = HelperReceipts.save_receipt(request, form_received, client)
            sales_received = HelperSale.save_sales_receipts(request, received)
            CreatePdf.create_pdf(received, sales_received, client)
            messages.success(request, 'Venta guardada exitosamente')
            messages.success(request, 'Se mando a imprimir el ticket')
        return redirect('sales:clear_cart')
    
#Crud receipts
class ReceiptRead(UserPassesTestMixin, ListView):
    model = Receipts
    template_name = 'receipts/table_receipt.html'
    form_class = FormReceiptFilter
    
    def test_func(self):
        return self.request.user.is_staff
    
    def get_queryset(self):
        queryset = super().get_queryset()
        form = self.form_class(self.request.GET)

        if form.is_valid():
            fecha = form.cleaned_data['fecha']
            # Filtrar los objetos según la fecha proporcionada
            queryset = queryset.filter(create__date=fecha)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class(self.request.GET)
        return context

class ReceiptAllView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_staff
    
    def get(self, request, *args, **kwarg):
        receipt_id = self.kwargs['pk']
        receipt_all = HelperReceipts.get_receipt_all(receipt_id)
        context = {
            'receipts' : receipt_all,
        }
        return render(request, 'receipts/table_receipt_all.html', context)

class ReceiptDelete(UserPassesTestMixin, DeleteView):
    model = Receipts
    template_name = 'receipts/receipt_delete.html'
    success_url = reverse_lazy('receipts:receipt_read')
    
    def test_func(self):
        return self.request.user.is_staff
    
    def post(self, request, *args, **kwargs):
        messages.success(self.request, 'Recibo eliminado exitosamente.')
        return super().post(request, *args, **kwargs)