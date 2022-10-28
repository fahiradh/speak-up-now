import datetime
from pyexpat import model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from . import models
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def add(request):
    if request.method == "POST":
        name = request.POST.get("name")
        title = request.POST.get("title")
        description = request.POST.get("description")
        contactable = request.POST.get("contactable")
        obj = models.curhatDong.objects.create(
            date=datetime.date.today(),
            name=name,
            title=title,
            description=description,
            contactable=contactable,
        )
        result = {
            'fields':{
                'date': obj.date,
                'name': obj.name,
                'title': obj.title,
                'description': obj.description,
                'contactable': obj.contactable,
            },
            'pk': obj.pk
        }
    return JsonResponse(result)

def show_riwayat(request):    
    # riwayat = models.curhatDong.objects.filter(user=request.user)    
    riwayat = models.curhatDong.objects.all()
    contexts = {
        'list': riwayat,
        # 'username' : request.user.username,
    }
    return render(request, 'riwayat-konsultasi.html', contexts)

def riwayat_json(request):
    riwayat = models.curhatDong.objects.all()
    # serialized_posts = serializers.serialize('json', riwayat)
    # print(serialized_posts)
    # context = {'riwayat': riwayat, 'serialized_posts': serialized_posts}
    return HttpResponse(serializers.serialize("json", riwayat), content_type="application/json")
    # return render(request, 'riwayat-konsultasi.html', context)

def delete_konsultasi(request, id):
    # task = models.curhatDong.objects.filter(id=id, user=request.user)
    task = models.curhatDong.objects.filter(id=id)
    task.delete()
    return HttpResponse()