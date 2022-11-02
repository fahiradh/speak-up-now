from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from laporan.models import laporan
from laporan_admin.models import laporanResponse
from laporan_admin.forms import laporanResponseForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def show_laporan_json(request):
    data_laporan = laporan.objects.all()
    return HttpResponse(serializers.serialize("json", data_laporan), content_type="application/json")

def show_response_json(request):
    data_response = laporanResponse.objects.all()
    return HttpResponse(serializers.serialize("json", data_response), content_type="application/json")

def delete_laporan(request, id):
    if request.method == 'DELETE':
        laporan_user = laporan.objects.get(pk=id)
        laporan_user.delete()
    return HttpResponse()

def show_laporan_user(request):
    return render(request, "laporan-user.html")

def show_detail_laporan(request,id):
    form = laporanResponseForm()
    data = laporan.objects.get(pk=id)
    context = {
        'form':form,
        'data':data,
        'id':id
    }
    return render(request, "detail-laporan-user.html", context)

@csrf_exempt
def add_response(request,id):
    if request.method == 'POST':
        form = laporanResponseForm(request.POST)
        id=id-1
        if form.is_valid():
            new_response = form.cleaned_data
            response = laporanResponse.objects.get(pk=id)
            response.admin_name = request.user.username
            response.case_name = laporan.objects.get(pk=id).case_name
            response.status_case = new_response['status_case']
            response.admin_response = new_response['message']
            response.save()        
            return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()