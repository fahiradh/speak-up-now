from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add, name='add'),
    path('json/', views.riwayat_json, name='riwayat-json'),
    path('', views.add, name='konsultasi'),
    path('delete/<int:id>', views.delete_konsultasi, name='delete'),
]