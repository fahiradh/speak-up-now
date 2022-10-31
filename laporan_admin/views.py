from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.contrib.auth.models import User
from laporan.models import laporan
from laporan_admin.models import laporanResponse
from laporan_admin.forms import laporanResponseForm

# Create your views here.
def show_laporan_json(request):
    data_laporan = laporan.objects.all()
    return HttpResponse(serializers.serialize("json", data_laporan), content_type="application/json")

def show_detail_json(request,id):
    if request.method == 'POST':
        laporan_detail= laporan.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", laporan_detail), content_type="application/json")

def delete_laporan(request):
    if request.method == 'DELETE':
        laporan_user = laporan.objects.get(pk=request.DELETE["id"])
        laporan_user.delete()
    return HttpResponse()

def show_laporan_user(request):
    return render(request, "laporan-user.html")

def show_detail_laporan(request,id):
    form = laporanResponseForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            new_data = form.cleaned_data        
            new_response = laporanResponse (
                laporan_user = laporan.objects.get(pk=request.POST.get('id')), # Hubungin ke laporan user
                admin_name = request.user.username,
                case_name = laporan.objects.get(pk=request.POST.get('id')).case_name, # Hubungin ke case pelapor
                status_case = new_data['status_case'],
                admin_response = new_data['admin_response'],
            )
            new_response.save()
            return HttpResponse()
    else:
        new_response = laporanResponseForm()
    
    context = {
        'form':form,
        'pk':id,
    }
    return render(request, "detail-laporan-user.html", context)

def reply_laporan_user(request):
    if request.method == 'POST':
        statusCase = request.POST.get('status_case')
        adminResponse = request.POST.get('admin_response')
        
        new_response = laporanResponse (
            laporan_user = laporan.objects.get(pk=request.POST["id"]), # Hubungin ke pelapor
            admin_name = request.user.username,
            case_name = laporan.objects.get(pk=request.POST["id"]).fields.case_name, # Hubungin ke case pelapor
            status_case = statusCase,
            admin_response = adminResponse,
        )
        new_response.save()
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()