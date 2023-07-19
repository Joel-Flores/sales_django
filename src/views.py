from django.views.generic import View
from django.shortcuts import render
class HomeView(View):
    def get(self, request, *args, **kwarg):
        context = {
            
        }
        return render(request, 'home.html', context, )