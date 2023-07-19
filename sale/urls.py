from django.urls import path

from .views import SaleListView
app_name = 'sale'

urlpatterns = [
    path('', SaleListView.as_view(), name='homesale')
]