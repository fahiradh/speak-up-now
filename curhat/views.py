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
            )
            data.save()
            return HttpResponse(status=204)
    else:
        form = forms.curhatForm()

    contexts = {
        'curhat' : models.curhatDong.objects.all().values(),
        'form' : form,
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
    context = {
        'data' : models.curhatDong.objects.get(pk=id)
    }
    return render(request, 'detail-form.html', context)
    
def show_curhat_details(request, i):
    form = replyCurhatForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            cd = form.cleaned_data

            form = curhatAdmin(
                title = cd['title'],
                description = cd['description']
            )
            form.save()
        details = curhatDong.objects.get(id=i)  
        form = replyCurhatForm()
        contexts = {
            'form': form,
            'details' : details
        }
        return render(request, 'curhat-details.html', contexts)
    else:
        form = replyCurhatForm()

    details = curhatDong.objects.get(id=i)  
    contexts = {
        'form': form,
        'details' : details
    }
    return render(request, 'curhat-details.html', contexts)