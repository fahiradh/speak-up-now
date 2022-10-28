from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from curhat_admin.views import show_table_curhat, show_curhat_details, table_json, show_curhat_details_example, show_table_curhat_example

app_name = 'curhat_admin'

urlpatterns = [
    path('', show_table_curhat, name='table-curhat'),
    path('curhat-details', show_curhat_details, name='curhat-details'),
    path('json', table_json, name='table-json'),
    path('table-example', show_table_curhat_example, name='table-curhat-example'),
    path('curhat-details-example', show_curhat_details_example, name='curhat-details-example'),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)