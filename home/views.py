from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from home.forms import LoginForm, SignUpForm
from home.models import Pengguna


def homepage(request):
    return render(request, 'homepage.html')

def register(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('home:homepage')
    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    form = LoginForm(request.POST)
    messages = None
    if request.method == 'POST':
        if form.is_valid():
            username= form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_konsulir:
                login(request, user)
                return redirect('curhat_admin:table-curhat')
            elif user is not None and (user.is_konsulir == False):
                login(request, user)
                return redirect('home:homepage')
            else:
                messages = 'Username atau Password salah!'
        else:
            messages = 'Error Validating Form'
    return render(request, 'login.html', {'form' : form, 'messages': messages})
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         user_type = Pengguna.objects.filter(request)
    #         if user.is_authenticated and user_type.is_konsulir == 1:
    #             return redirect('curhat_admin:table-curhat')
    #         elif user.is_authenticated and user_type.is_konsulir == 0:
    #             return redirect('home:homepage')
    #     else:
    #         messages.info(request, 'Username atau Password salah!')
    # context = {}
    # return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('home:homepage')