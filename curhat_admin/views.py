import json as JSON
from django.shortcuts import render, redirect
from curhat.models import curhatDong
from curhat_admin.forms import replyCurhatForm
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import datetime

from curhat_admin.models import curhatAdmin

# Create your views here.
@login_required(login_url='/login')
def show_table_curhat(request):
    return render(request, 'table-curhat.html')

def table_json(request):
    curhatan = curhatDong.objects.all()
    return HttpResponse(serializers.serialize('json', curhatan), content_type='application/json')

def delete_json(request, i):
    obj = curhatDong.objects.get(id=i)

    if request.method == 'DELETE':
        obj.delete()
        
    return HttpResponse('')

@login_required(login_url='/login')
def show_curhat_details(request, i):
    form = replyCurhatForm()
    details = curhatDong.objects.get(id=i)  
    if (details.contactable == "N"):
        message = "Mode: No need consultation in interactive mode"
    else:
        message = "Mode: Need consultation in interactive mode"
    contexts = {
        'details' : details,
        'message' : message,
        'form' : form,
        'id' : i
    }
    return render(request, 'curhat-details.html', contexts)

@csrf_exempt
def add_reply(request, i):
    form = replyCurhatForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            cd = form.cleaned_data
            data = curhatAdmin(
                date = datetime.date.today(),
                admin_name = request.user.username,
                id = i,
                title = cd['title'],
                description = cd['description'],
            )
            data.save()
            return HttpResponse()
    else:
        form = replyCurhatForm()

    contexts = {
        'curhat' : curhatAdmin.objects.all().values(),
        'form' : form,
    }

    return render(request, 'curhat-details.html', contexts)

def reply_json(request, i):
    reply = curhatAdmin.objects.filter(id=i)
    return HttpResponse(serializers.serialize('json', reply), content_type='application/json')

@csrf_exempt
def add_reply_flutter(request):
    if request.method == "POST":
        data = JSON.loads(request.body)

        reply = curhatAdmin(admin_name = data["adminName"],
                            date = data["date"],
                            title = data["title"],
                            description = data["description"],
                            id = data["pk"],
        )

        try:
            reply.save()
        except:
            return JsonResponse({
            "success": "Error"
        })
        else:
            return JsonResponse({
            "success": "Reply berhasil terkirim!",
        })
    
@csrf_exempt
def delete_json_flutter(request, i):
    obj = curhatDong.objects.get(id=i)

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
