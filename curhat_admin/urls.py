from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from curhat_admin.views import show_table_curhat, show_curhat_details, table_json, delete_json, reply_json, add_reply, add_reply_flutter, delete_json_flutter
app_name = 'curhat_admin'

urlpatterns = [
    path('', show_table_curhat, name='table-curhat'),
    path('curhat-details/<int:i>', show_curhat_details, name='curhat-details'),
    path('add-reply/<int:i>', add_reply, name='add-reply'),
    path('reply-json/<int:i>', reply_json, name='reply-json'),
    path('json', table_json, name='table-json'),
    path('delete/<int:i>', delete_json, name='delete-json'),
    path('add-reply-flutter', add_reply_flutter, name='add-reply-flutter'),
    path('delete-flutter/<int:i>', delete_json_flutter, name='delete-json-flutter'),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
