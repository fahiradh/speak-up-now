from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from . import models
from .forms import laporanForm
from laporan_admin import models
from home import models

def add_laporan(request):
    form = laporanForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user_id = request.COOKIES['user']
            name = request.POST.get('name')
            phone_num = request.POST.get('phone_num')
            email = request.POST.get('email')
            case_name = request.POST.get('case_name')
            victim_name = request.POST.get('victim_name')
            victim_description = request.POST.get('victim_description')
            crime_place = request.POST.get('crime_place')
            chronology = request.POST.get('chronology')
            new_laporan = models.laporan(name = name, phone_num = phone_num, email = email, case_name = case_name, victim_name = victim_name,
                                        victim_description = victim_description, crime_place = crime_place, chronology = chronology)
            new_laporan.save()
            new_response = models.laporanResponse(laporan_user=new_laporan, admin_name="-", case_name=case_name, status_case=None, admin_response="-")
            new_response.save()
        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def show_laporan(request):
    form_gen = laporanForm()
    context = {
        'form' : form_gen
    }
    return render(request, 'laporan.html', context)

def show_json(request):
    data = models.laporan.objects
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def delete_report(request, id):
    data = models.laporan.objects.get(pk=id)
    data.delete()
    return HttpResponse(b"DELETED", status=201)

def detail_laporan(request, id):
    data = models.laporan.objects.get(pk=id)
    context = {'item' : data}
    return render(request, 'laporan-detail.html', context)