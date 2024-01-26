from django.urls import path, include
from myapp.views import index, index_item, add_item


app_name = "myapp"

urlpatterns = [
    path('', index),
    path('<int:my_id>/', index_item, name="detail"),
    path('additem/', add_item, name="add_item")
]


