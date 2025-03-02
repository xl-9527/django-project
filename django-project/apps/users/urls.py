from django.urls import re_path
from . import views

app_name = 'users'

urlpatterns = [
    re_path(r'^registry/$', views.RegistryView.as_view(), name='registry')
]
