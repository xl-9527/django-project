# django-project/urls.py
from django.urls import re_path, include

urlpatterns = [
    re_path(r'^', include('users.urls', namespace='users'))
]
