import datetime
import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core import serializers
from django.http import HttpResponse
from . import models, forms
from curhat_admin.models import curhatAdmin
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
@login_required(login_url='/login')
def add(request):
    if request.method == "POST":
        form = forms.curhatForm(request.POST)
        if form.is_valid():
            data = models.curhatDong(
                user = request.user,
                date = datetime.date.today(),
                name = form.data['name'],
                title = form.data['title'],
                description = form.data['description'],
                contactable = form.data['contactable']
            )
            data.save()
            return HttpResponse()
    else:
        form = forms.curhatForm()

    contexts = {
        'curhat' : models.curhatDong.objects.filter(user = request.user.id),
        'form' : form,
    }

    return render(request, 'riwayat-konsultasi.html', contexts)

@login_required(login_url='/login')
def show_laporan(request):
    form_gen = forms.curhatForm()
    contexts = {
        'form' : form_gen,
        'data' : models.curhatDong.objects.all().values(),
    }
    return render(request, 'riwayat-konsultasi.html', contexts)

def riwayat_json(request):
    riwayat = models.curhatDong.objects.filter(user = request.user.id)
    return HttpResponse(serializers.serialize("json", riwayat), content_type="application/json")

@login_required(login_url='/login')
def delete_konsultasi(request, id):
    data = models.curhatDong.objects.get(pk=id)
    data.delete()
    return HttpResponse()

@login_required(login_url='/login')
def detail_form(request, id):
    data = models.curhatDong.objects.get(pk=id)
    if (data.contactable == "N"):
        message = "Mode: No need consultation in interactive mode"
    else:
        message = "Mode: Need consultation in interactive mode"
    try:
        reply = curhatAdmin.objects.get(pk=id)
        context = {
            'data' : models.curhatDong.objects.get(pk=id),
            'message' : message,
            'reply' : reply
    }
    except:
        context = {
            'data' : models.curhatDong.objects.get(pk=id),
            'message' : message,
        }
    return render(request, 'detail-form.html', context)

@csrf_exempt
def add_konsultasi_flutter(request):
    if request.method == "POST":
        data = json.loads(request.body)
        consultation = models.curhatDong(
                    user =  request.user,
                    date = datetime.date.today(),
                    title = data["title"],
                    description = data["description"],
                    contactable = data['contactable'],
                    id = data["pk"],
        )
        

        try:
            consultation.save()
        except:
            return JsonResponse({
            "success": "Error"
        })
        else:
            return JsonResponse({
            "success": "Konsultasi berhasil disimpan!",
        })

@csrf_exempt
def delete_json_flutter(request, i):
    obj = models.curhatDong.objects.get(id=i)

    try:
        obj.delete()
    except:
        return JsonResponse({
        "success": "Error"
    })
    else:
        return JsonResponse({
        "success": "Konsultasi terhapus!",
    })