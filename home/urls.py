from home.views import homepage, register, login_user,logout_user
from django.urls import path

app_name = 'home'

urlpatterns= [
    path('', homepage, name='homepage'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout')
]