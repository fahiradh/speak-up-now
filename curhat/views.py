import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core import serializers
from django.http import HttpResponse
from . import models, forms
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def add(request):
    if request.method == "POST":
        form = forms.curhatForm(request.POST)
        if form.is_valid():
            data = models.curhatDong(
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
        'curhat' : models.curhatDong.objects.all().values(),
        'form' : form,
    }

    return render(request, 'riwayat-konsultasi.html', contexts)

def show_laporan(request):
    form_gen = forms.curhatForm()
    contexts = {
        'form' : form_gen,
        'data' : models.curhatDong.objects.all().values(),
    }
    return render(request, 'riwayat-konsultasi.html', contexts)

def riwayat_json(request):
    riwayat = models.curhatDong.objects.all()
    return HttpResponse(serializers.serialize("json", riwayat), content_type="application/json")

def delete_konsultasi(request, id):
    data = models.curhatDong.objects.get(pk=id)
    data.delete()
    return HttpResponse()

def detail_form(request, id):
    data = models.curhatDong.objects.get(pk=id)
    if (data.contactable == "N"):
        message = "Mode: No need consultation in interactive mode"
    else:
        message = "Mode: Need consultation in interactive mode"
    context = {
        'data' : models.curhatDong.objects.get(pk=id),
        'message' : message
    }
    return render(request, 'detail-form.html', context)