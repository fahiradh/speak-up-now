from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from home.forms import LoginForm, SignUpForm
from home.models import Pengguna
@csrf_exempt
def register(request):
    form = SignUpForm()
    if form.is_valid():
        form.save()
        return JsonResponse(
            {
                "status": True,
                "message": "Registration success!",
            }, status = 200
        )
    else:
        return JsonResponse (
            {
                "status": False,
                "message": "Registration failed!",
                "details": form.errors
            }, status= 400
        )

@csrf_exempt
def login(request):
    form = LoginForm(request.POST)
    username = form.data.get('username')
    password = form.data.get('username')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            userId = Pengguna.objects.get(username = username).pk
            # Redirect to a success page.
            return JsonResponse({
            "status": True,
            "message": "Successfully Logged In!",
            "data": userId
            # Insert any extra data if you want to pass data to Flutter
            }, status=200)
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