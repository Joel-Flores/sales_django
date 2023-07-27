from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import *
app_name = 'receipts'

urlpatterns = [
    path('pay_order/', login_required(PayOrder.as_view()), name='pay')
]