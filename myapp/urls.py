from django.urls import path, include
from myapp.views import index, contacts, index_item

urlpatterns = [
    path('hello/', index),
    path('hello/<int:my_id>', index_item),
    path('contacts/', contacts),
]