from django import forms

from receipts.models import Receipts

class FormSearchReceipt(forms.ModelForm):
    class Meta:
        model = Receipts
        fields = ['sale_total']
        labels = {'sale_total' : 'codigo del recibo'}
        widgets = {
            'sale_total' : forms.TextInput(
                attrs = {
                    'class' : 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                    'placeholder': 'ingrese el codigo del recibo'
                }
            ),
        }