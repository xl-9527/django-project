from django.shortcuts import render
from django.views import View
import logging

log = logging.getLogger('django')

# Create your views here.
class RegistryView(View):
    def get(self, request):
        return render(request, 'users/registry.html')

    def post(self, request):
        # log.info(request)
        pass