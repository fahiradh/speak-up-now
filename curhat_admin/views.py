from django.shortcuts import render
from curhat.models import curhatDong

# Create your views here.
def show_table_curhat(request):
    return render(request, "table-curhat.html")