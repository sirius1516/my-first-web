from django.urls import path, include
from myapp.views import index, contacts

urlpatterns = [
    path('hello/', index),
    path('contacts/', contacts),
]