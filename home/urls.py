from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import *
app_name = 'home'

urlpatterns = [
    path('', login_required(HomeView.as_view()), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('super_user/', HomeAdminView.as_view(), name='super_admin')
]