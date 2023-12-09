from django.urls import path, include
from myapp.views import index, contacts, index_item

app_name = "myapp"

urlpatterns = [
    path('hello/', index),
    path('hello/<int:my_id>/', index_item, name="detail"),
    path('contacts/', contacts),
]
