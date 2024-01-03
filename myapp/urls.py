from django.urls import path, include
from myapp.views import index, index_item

app_name = "myapp"

urlpatterns = [
    path('', index),
    path('<int:my_id>/', index_item, name="detail"),
]
