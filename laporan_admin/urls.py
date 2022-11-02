from django.urls import path
from laporan_admin.views import show_laporan_user, show_detail_laporan, add_response, show_response_json, show_laporan_json, delete_laporan
from django.conf.urls.static import static
from django.conf import settings

app_name = 'laporan_admin'

urlpatterns = [
    path('', show_laporan_user, name='show_laporan_user'),
    path('detail/<int:id>', show_detail_laporan, name='show_detail_laporan'),
    path('add-response/<int:id>', add_response, name='add_response'),
    path('json/', show_laporan_json, name='show_laporan_json'),
    path('response/json/', show_response_json, name='show_response_json'),
    path('delete/<int:id>', delete_laporan, name='delete_laporan'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)