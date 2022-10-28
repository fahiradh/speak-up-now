from django.urls import path
from . import views

urlpatterns = [
    # path('', views.show_form, name='show-form'),
    path('add/', views.add, name='add'),
    path('json/', views.riwayat_json, name='riwayat-json'),
    path('', views.show_riwayat, name='konsultasi'),
    path('delete/<int:id>', views.delete_konsultasi, name='delete'),
]