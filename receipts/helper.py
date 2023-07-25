from .models import Clients
from .models import Receipts
from src.helper import HelperApp

class HelperClients():
    def search_client(form):
        nit = form.cleaned_data['nit']
        name = form.cleaned_data['name']
        try:
            client = Clients.objects.get(nit=nit, name=name)
        except Clients.DoesNotExist:
            client = Clients(nit=nit)
            client.name = form.cleaned_data['name']
            client.save()
        return client
    
    def check_pay(request, form):
        total = HelperApp.get_total(request)
        received = form.cleaned_data['received']
        return True if received >= total else False

class HelperReceipts():
    def save_receipt(request, form, client : Clients) -> type[Receipts]:
        total = HelperApp.get_total(request)
        received = form.cleaned_data['received']
        receipt = Receipts(
            sale_total=total,
            received = received,
            change = round((received - total), 1),
            client = client
        )
        receipt.save()
        return receipt