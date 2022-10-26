from django.urls import path
from . import views

urlpatterns = [
    path('', views.curhat, name='curhat'),
]