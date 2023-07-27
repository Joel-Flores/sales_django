from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import *
app_name = 'sales'

urlpatterns = [
    path('add_to_cart_food/<int:pk>/', login_required(AddCart.as_view()), name='add_food'),
    path('add_to_card_soda/<int:pk>/', login_required(AddCart.as_view()), name='add_soda'),
    path('delete_order_to_cart/<int:pk>/', login_required(DeteleOrder.as_view()), name='delete_order'),
    path('clear_cart/', login_required(ClearCart.as_view()), name='clear_cart')
]