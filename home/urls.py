from home.views import homepage, register, login_user,logout_user, validate_username
from django.urls import path

app_name = 'home'

urlpatterns= [
    path('', homepage, name='homepage'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/validate-username/', validate_username, name='validate-username')
]