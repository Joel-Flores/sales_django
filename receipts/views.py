from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View

from src.create_pdf import CreatePdf
from src.helper import HelperApp
from sales.helper import HelperSale

from .helper import HelperClients
from .helper import HelperReceipts

from .forms import FormClient
from .forms import FormReceipt

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
        return render(request, 'view_orders.html', context, )
    
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
        return redirect('sales:clear_cart')