from django.urls import path

from .views import *
app_name = 'sale'

urlpatterns = [
    path('', ProductRead.as_view(), name = 'read'),
    path('create/', ProductCreate.as_view(), name = 'create'),
    path('update/<int:pk>/', ProductUpdate.as_view(), name = 'update'),
    path('delete/<int:pk>/', ProductDelete.as_view(), name = 'delete')
]