from django.urls import path
from . import views

app_name = 'user_page'

urlpatterns = [
    path('', views.show_user_page, name='show_user_page'),

]