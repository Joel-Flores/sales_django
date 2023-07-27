from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *
app_name = 'product'

urlpatterns = [
    path('product_name_read/', login_required(ProductRead.as_view()), name = 'product_read'),
    path('product_name_create/', login_required(ProductCreate.as_view()), name = 'product_create'),
    path('product_name_update/<int:pk>/', login_required(ProductUpdate.as_view()), name = 'product_update'),
    path('product_name_delete/<int:pk>/', login_required(ProductDelete.as_view()), name = 'product_delete'),
    path('product_type_read/', login_required(ProductTypeRead.as_view()), name = 'product_type_read'),
    path('product_type_create/', login_required(ProductTypeCreate.as_view()), name = 'product_type_create'),
    path('product_type_update/<int:pk>/', login_required(ProductTypeUpdate.as_view()), name = 'product_type_update'),
    path('product_type_delete/<int:pk>/', login_required(ProductTypeDelete.as_view()), name = 'product_type_delete'),
] 