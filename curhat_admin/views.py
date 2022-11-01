from django.shortcuts import render, redirect
from curhat.models import curhatDong
from curhat_admin.forms import replyCurhatForm
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import datetime

from curhat_admin.models import curhatAdmin

# Create your views here.
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
        'form' : form
    }
    return render(request, 'curhat-details.html', contexts)

@csrf_exempt
def add_reply(request):
    form = replyCurhatForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            cd = form.cleaned_data
            data = curhatAdmin(
                date = datetime.date.today(),
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

def reply_json(request):
    # reply_user = curhatDong.objects.get(id=i).user
    reply = curhatAdmin.objects.all()
    return HttpResponse(serializers.serialize('json', reply), content_type='application/json')