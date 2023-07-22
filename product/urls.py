from django.urls import path

from .views import *
app_name = 'product'

urlpatterns = [
    path('product_name_read/', ProductRead.as_view(), name = 'product_read'),
    path('product_name_create/', ProductCreate.as_view(), name = 'product_create'),
    path('product_name_update/<int:pk>/', ProductUpdate.as_view(), name = 'product_update'),
    path('product_name_delete/<int:pk>/', ProductDelete.as_view(), name = 'product_delete')
] 