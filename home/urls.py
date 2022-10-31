from home.views import homepage, register, login
from django.urls import path

app_name = 'home'

urlpatterns= [
    path('', homepage, name='homepage'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
]