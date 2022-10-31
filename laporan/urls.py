from django.urls import path
from . import views

app_name = 'laporan'

urlpatterns = [
    path('', views.show_laporan, name='show_laporan'),
    path('detail/<int:id>', views.detail_laporan, name='detail_laporan'),
    path('add-laporan/', views.add_laporan, name = 'add_laporan'),
    path('json/', views.show_json, name='show_json'),
    path('delete/<int:id>', views.delete_report, name='delete_report')

]