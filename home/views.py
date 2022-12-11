from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from home.forms import LoginForm, SignUpForm
from home.models import Pengguna
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

def homepage(request):
    list = Pengguna.objects.all()
    count_admin = 0
    count_user = 0
    for i in list:
        if i.is_konsulir == True:
            count_admin += 1
        elif i.is_konsulir == False and i.is_staff == False:
            count_user += 1
    context = {
        'jumlah_admin' : count_admin,
        'jumlah_user' : count_user
    }
    return render(request, 'homepage.html', context)

def register(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:homepage')
    context = {'form': form}
    return render(request, 'register.html', context)

def validate_username(request):
    username = request.GET.get('username')
    data = {
        'is_taken': Pengguna.objects.filter(username=username).exists()
    }
    return JsonResponse(data)

@csrf_exempt
def login_user(request):
    form = LoginForm(request.POST)

    messages = None
    if request.method == 'POST':
        if form.is_valid():
            username= form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None and user.is_konsulir:
                auth_login(request, user)
                return redirect('home:homepage')
            elif user is not None and (user.is_konsulir == False):
                auth_login(request, user)
                return redirect('home:homepage')
            else:
                messages = 'Username atau Password salah!'
                JsonResponse({
                "status": False,
                "message": "Failed to Login, check your email/password."
                }, status=401)
        else:
            messages = 'Error Validating Form'
    return render(request, 'login.html', {'form' : form, 'messages': messages})

def logout_user(request):
    logout(request)
    return redirect('home:homepage')

@csrf_exempt
def userdetail(request):
    form = LoginForm(request.POST) 
    username= form.data.get('username')
    password = form.data.get('password')

    user = authenticate(username= username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            return JsonResponse({
                "status": True,
                "message": "Successfully Logged In!",
                "username": username
            }, status= 200)

        else:
            return JsonResponse({
            "status": False,
            "message": "Failed to Login, Account Disabled."
            }, status=401)

    else:
        return JsonResponse({
        "status": False,
        "message": "Failed to Login, check your password."
        }, status=401)