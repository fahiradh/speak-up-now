from django.urls import path
from . import views

urlpatterns = [
    path('', views.curhat, name='curhat'),
    path('success/', views.success, name='success'),
    path('json/', views.riwayat_json, name='riwayat-json'),
    path('riwayat-konsultasi/', views.show_riwayat, name='riwayat-konsultasi')
]