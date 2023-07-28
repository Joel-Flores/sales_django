from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import *
app_name = 'receipts'

urlpatterns = [
    path('pay_order/', login_required(PayOrder.as_view()), name='pay'),
    path('receipt_read/', login_required(ReceiptRead.as_view()), name='receipt_read'),
    path('receipt_all/<int:pk>', login_required(ReceiptAllView.as_view()), name='receipt_all'),
    path('receipt_delete/<int:pk>/', login_required(ReceiptDelete.as_view()), name='receipt_delete')
]