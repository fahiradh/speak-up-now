
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from curhat_admin.views import show_table_curhat, show_curhat_details

app_name = 'curhat_admin'

urlpatterns = [
    path('', show_table_curhat, name='table-curhat'),
    path('curhat-details', show_curhat_details, name='curhat-details'),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)