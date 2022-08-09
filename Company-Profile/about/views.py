from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'Onasis Indonesia',
        'heading': 'Selamat Datang di About',
    }
    return render(request, 'about/index.html', context)