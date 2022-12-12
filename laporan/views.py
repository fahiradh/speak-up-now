from pyexpat import model
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
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
from django.views.decorators.csrf import csrf_exempt
import json as JSON

@csrf_exempt
def add_laporan(request):
    if request.method == 'POST':
        form = laporanForm(request.POST)
        if form.is_valid():
            user = request.user
            name = request.POST['name']
            phone_num = request.POST['phone_num']
            email = request.POST['email']
            case_name = request.POST['case_name']
            victim_name = request.POST['victim_name']
            victim_description = request.POST['victim_description']
            crime_place = request.POST['crime_place']
            chronology = request.POST['chronology']
            new_laporan = models.laporan(user = user,name = name, phone_num = phone_num, email = email, case_name = case_name, victim_name = victim_name,
                                        victim_description = victim_description, crime_place = crime_place, chronology = chronology)
            new_laporan.save()
            new_response = models.laporanResponse(laporan_user=new_laporan, admin_name="-", case_name=case_name, status_case=None, admin_response="-")
            new_response.save()
        return JsonResponse({
            "success": "Reply berhasil terkirim!"
        })

    return JsonResponse({
            "success": "Error",
        })

@login_required(login_url='/login')
def show_laporan(request):
    form_gen = laporanForm()
    context = {
        'form' : form_gen
    }
    return render(request, 'laporan.html', context)

@login_required(login_url='/login')
def show_json(request):
    data = models.laporan.objects.filter(user = request.user.id)
    print(data)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def delete_report(request, id):
    data = models.laporan.objects.get(pk=id)
    data.delete()
    print(id)
    return HttpResponse(b"DELETED", status=201)

@login_required(login_url='/login')
def detail_laporan(request, id):
    laporan = models.laporan.objects.get(pk=id)
    response = models.laporanResponse.objects.get(laporan_user=id)
    context = {'item' : laporan,
            'response' : response
            }
    return render(request, 'laporan-detail.html', context)

@csrf_exempt
def add_laporan_flutter(request):
    print('halo')
    if request.method == "POST":
        data = JSON.loads(request.body)
        user = models.laporan.objects.filter(user = data['id'])
        laporan = models.laporan(
                            user = request.user,
                            name = data['name'], 
                            phone_num = data['phone_num'], 
                            email = data['email'], 
                            case_name = data['case_name'], 
                            victim_name = data['victim_name'],
                            victim_description = data['victim_description'], 
                            crime_place = data['crime_place'], 
                            chronology = data['chronology'],    
        )

        try:
            laporan.save()
        except:
            return JsonResponse({
            "success": "Error"
        })
        else:
            return JsonResponse({
            "success": "Reply berhasil terkirim!",
        })