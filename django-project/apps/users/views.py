from django.shortcuts import render
from django.views import View

# Create your views here.
class RegistryView(View):
    def get(self, request):
        return render(request, 'users/registry.html')
    pass