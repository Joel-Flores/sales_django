from django.urls import path

from .views import *
app_name = 'product'

urlpatterns = [
    path('product_name_read/', ProductRead.as_view(), name = 'product_read'),
    path('product_name_create/', ProductCreate.as_view(), name = 'product_create'),
    path('product_name_update/<int:pk>/', ProductUpdate.as_view(), name = 'product_update'),
    path('product_name_delete/<int:pk>/', ProductDelete.as_view(), name = 'product_delete'),
    path('product_type_read/', ProductTypeRead.as_view(), name = 'product_type_read'),
    path('product_type_create/', ProductTypeCreate.as_view(), name = 'product_type_create'),
    path('product_type_update/<int:pk>/', ProductTypeUpdate.as_view(), name = 'product_type_update'),
    path('product_type_delete/<int:pk>/', ProductTypeDelete.as_view(), name = 'product_type_delete'),
] 