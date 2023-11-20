from django.urls import path, include
from myapp.views import index

urlpatterns = [
    path('', index),
]