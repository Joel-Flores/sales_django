from django.urls import path

from .views import *
app_name = 'sales'

urlpatterns = [
    path('add_to_cart_food/', AddCartFood.as_view(), name='add_food'),
    path('add_to_card_soda/', AddCartSoda.as_view(), name='add_soda'),
    path('delete_order_to_cart/<int:pk>/', DeteleOrder.as_view(), name='delete_order'),
    path('clear_cart/', ClearCart.as_view(), name='clear_cart')
]