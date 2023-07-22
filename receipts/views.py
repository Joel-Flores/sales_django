from django.shortcuts import render
from django.views import View

# Create your views here.
class PayOrder(View):
    def get(self, request, *args, **kwarg):
        context = {
            
        }
        return render(request, 'home.html', context, )