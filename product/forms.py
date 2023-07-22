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