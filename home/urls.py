from home.views import *
from django.urls import path

app_name = 'home'

urlpatterns= [
    path('', homepage, name='homepage'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/validate-username/', validate_username, name='validate-username'),
    path('user-details/', userdetail, name='userdetails'),
    path('register-ajax/', register_ajax, name='registerajax'),
    path('logout-ajax/', logout_flutter, name='logoutajax')
]