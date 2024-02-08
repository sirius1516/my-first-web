from django.urls import path, include
from myapp.views import index, index_item, add_item, update_item, delete_item


app_name = "myapp"

urlpatterns = [
    path('', index, name='index'),
    path('<int:my_id>/', index_item, name="detail"),
    path('additem/', add_item, name="add_item"),
    path("update_item/<int:my_id>/", update_item, name="update_item"),
    path("deleteitem/<int:my_id>", delete_item, name="delete_item"),
]


