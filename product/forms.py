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