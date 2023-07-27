from django import forms
from django.contrib.auth.forms import UserCreationForm

from receipts.models import Receipts

class CustomUserForm(UserCreationForm):
    username = forms.CharField(
        label= 'Nuevo usario',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingresa tu username',
                'class': 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'
            }
        )
    )
    password1 = forms.CharField(
        label= 'Contraña',
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                'placeholder': 'Ingresa contraseña',
                'class': 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'
            }
        )
    )
    password2 = forms.CharField(
        label= 'Repite tu contraña',
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                'placeholder': 'Confirma contraseña',
                'class': 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'
            }
        )
    )
    first_name = forms.CharField(
        label= 'Nombre del usuario',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingresa tu nombre',
                'class': 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'
            }
        )
    )
    last_name = forms.CharField(
        label= 'Apellido del usuario',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingresa tu apellido',
                'class': 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'
            }
        )
    )
    class Meta(UserCreationForm.Meta):
        # Puedes modificar más configuraciones utilizando la clase Meta
        # Por ejemplo, cambiar el orden de los campos en el formulario
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name']

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