from django.urls import path, include
from myapp.views import index, index_item
from django.conf import settings
from django.conf.urls.static import static

app_name = "myapp"

urlpatterns = [
    path('', index),
    path('<int:my_id>/', index_item, name="detail"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)