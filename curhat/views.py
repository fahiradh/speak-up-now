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
                date = form.data['date_year'] + "-" + form.data['date_month'] + "-" + form.data['date_day'],
                name = form.data['name'],
                title = form.data['title'],
                description = form.data['description'],
            )
            data.save()
            return redirect('/curhat/')
    else:
        form = forms.curhatForm()

    contexts = {
        'curhat' : models.curhatDong.objects.all().values(),
        'form' : form,
    }

    return render(request, 'curhat.html', contexts)

def riwayat_json(request):
    riwayat = models.curhatDong.objects.all()
    return HttpResponse(serializers.serialize("json", riwayat), content_type="application/json")

def delete_konsultasi(request, id):
    task = models.curhatDong.objects.get(pk=id)
    task.delete()
    return HttpResponse()