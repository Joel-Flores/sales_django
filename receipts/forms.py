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
                attrs={
                    'value': '0',
                    'class': 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                    'placeholder': 'Ingrese el nit del cliente'
                }
            ),
            'name' : forms.TextInput(
                attrs={
                    'class': 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                    'placeholder': 'Ingrese el nombre del cliente'
                }
            )
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
        widgets = {
            'received': forms.TextInput(
                attrs={
                    'class': 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                    'placeholder': 'Ingrese el pago en Bs'
                }
            ),
        }