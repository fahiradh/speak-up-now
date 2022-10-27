from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core import serializers
from django.http import HttpResponse
from . import forms, models

# Create your views here.
def curhat(request):
    post_form = forms.curhatForm(request.POST or None)
    if request.method == "POST":
        if post_form.is_valid():
            curhatData = models.curhatDong(
                date = post_form.data['date_year'] + "-" + post_form.data['date_month'] + "-" + post_form.data['date_day'],
                name = post_form.data['name'],
                title = post_form.data['title'],
                description = post_form.data['description'],
                contactable = post_form.data['contactable'],
            )
            curhatData.save()
    else:
        post_form = forms.curhatForm()
            
    contexts = {
        'curhat': models.curhatDong.objects.all().values(),
        'form': post_form,
    }
    return render(request, 'curhat.html', contexts)

def show_riwayat(request):    
    # riwayat = models.curhatDong.objects.filter(user=request.user)    
    riwayat = models.curhatDong.objects.all().values(),
    contexts = {
        'list': riwayat,
        # 'curhat': models.curhatDong.objects.all().values(),
        # 'username' : request.user.username,
    }
    return render(request, 'riwayat-konsultasi.html', contexts)

# @login_required(login_url='login/')
# def riwayat_json(request):
#     # riwayat = models.curhatDong.objects.filter(user=request.user)
#     riwayat = models.curhatDong.objects.all(),
#     return HttpResponse(serializers.serialize('json', riwayat), content_type='application/json')

def riwayat_json(request):
    riwayat = models.curhatDong.objects.all()
    serialized_posts = serializers.serialize('json', riwayat)
    print(serialized_posts)
    context = {'riwayat': riwayat, 'serialized_posts': serialized_posts}
    return render(request, 'riwayat-konsultasi.html', context)

def success(request):
    return render(request, 'success.html')