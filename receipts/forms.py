from django import forms

from .models import Clients, Receipts

class FormClient(forms.ModelForm):
    class Meta:
        model = Clients
        fields = [
            'name', 'nit',
        ]
        labels = {
            'name' : 'ingrese el nombre del usuario',
            'nit' : 'ingrese el nit o ci del cliente',
        }
        widgets = {
            'nit': forms.NumberInput(
                attrs={'value': '0'}
            ),
        }

class FormReceipt(forms.ModelForm):
    class Meta:
        model = Receipts
        fields = [
            'received'
        ]
        labels = {
            'received' : 'ingrese monto que pago el cliente'
        }
    