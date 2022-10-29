from django.shortcuts import render, redirect
from curhat.models import curhatDong
from curhat_admin.forms import replyCurhatForm
from django.http import HttpResponse
from django.core import serializers

from curhat_admin.models import curhatAdmin

# Create your views here.
def show_table_curhat(request):
    return render(request, 'table-curhat.html')

def table_json(request):
    curhatan = curhatDong.objects.all()
    return HttpResponse(serializers.serialize('json', curhatan), content_type='application/json')

def delete_json(request, id):
    task = curhatDong.objects.get(id=id)

    if request.method == 'DELETE':
        task.delete()
        
    return HttpResponse('')

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

def show_curhat_details_example(request):
    return render(request, "curhat-details-example.html")

def show_table_curhat_example(request):
    return render(request, 'table-curhat-example.html')