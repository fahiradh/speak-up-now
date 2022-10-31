from django.shortcuts import render

# Create your views here.
def show_user_page(request):
    return render(request, 'user-page.html')