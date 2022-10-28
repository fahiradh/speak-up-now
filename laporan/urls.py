from django.urls import path
from . import views

app_name = 'laporan'

urlpatterns = [
    path('', views.show_laporan, name='show_laporan'),
    path('form-laporan/', views.form_laporan, name='form_laporan'),
    path('add-laporan/', views.add_laporan, name = 'add_laporan'),
    path('json/', views.show_json, name='show_json')
]