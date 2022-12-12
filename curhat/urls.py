from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add, name='add'),
    path('json/', views.riwayat_json, name='riwayat-json'),
    path('', views.show_laporan, name='konsultasi'),
    path('delete/<int:id>', views.delete_konsultasi, name='delete'),
    path('detail/<int:id>', views.detail_form, name='detail'),
    path('add-konsultasi-flutter', views.add_konsultasi_flutter, name='add-reply-flutter'),
    path('delete-flutter/<int:i>', views.delete_json_flutter, name='delete-json-flutter'),
]