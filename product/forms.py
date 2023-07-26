from django import forms

from .models import ProductName
from .models import ProductType

class ProductNameForm(forms.ModelForm):
    class Meta:
        model = ProductName
        fields = [
            'name',
            'price',
            'type'
        ]
        labels = {
            'name' : 'nombre del producto',
            'price' : 'precio del producto',
            'type' : 'tipo de producto'
        }

class ProductTypeForm(forms.ModelForm):
    class Meta:
        model = ProductType
        fields = [
            'name',
        ]
        labels = {
            'name' : 'nombre del type de producto',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                    'placeholder': ''
                }
            ),
        }
        