from django.urls import path

from .views import *
app_name = 'receipts'

urlpatterns = [
    path('pay_order/', PayOrder.as_view(), name='pay')
]