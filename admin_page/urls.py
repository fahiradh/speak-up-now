from django.urls import path
from admin_page.views import show_admin_page

app_name = 'user_page'

urlpatterns = [
    path('', show_admin_page, name='show_admin_page'),

]