from home.views import homepage, register
from django.urls import path

app_name = 'home'

urlpatterns= [
    path('', homepage, name='homepage'),
    path('register/', register, name='register'),
]