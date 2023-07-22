from django import forms

from .models import Clients

class FormClient(forms.ModelForm):
    class Meta:
        model = Clients
        fields = [
            'name',
        ]
        labels = {
            'name' : 'ingrese el nombre del usuario',
        }
    