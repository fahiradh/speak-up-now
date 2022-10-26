from django.shortcuts import render, redirect
from .forms import curhatForm
from .models import curhatDong

# Create your views here.
def curhat(request):
    post_form = curhatForm(request.POST or None)
    if request.method == "POST":
        if post_form.is_valid():
            post_form.save()
            return redirect('/curhat/')
    else:
        post_form = curhatForm()
            
    posts = curhatDong.objects.all()
    contexts = {
        'posts': posts,
        'form': post_form,
    }
    return render(request, 'curhat.html', contexts)
