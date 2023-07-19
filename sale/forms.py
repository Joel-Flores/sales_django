from django import forms

from .models import ProductName

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
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'}),
            'price' : forms.NumberInput(),
            'type' : forms.Select()
        }