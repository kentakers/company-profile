from multiprocessing import context
from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': 'About Us',
        'heading': 'Selamat Datang di About Us',
        'app_css': 'about/css/styles.css',
    }
    return render(request, 'about/index.html', context)


def visionMission(request):
    context = {
        'title': 'Vision, Mission & Value',
        'heading': 'Vision, Mission & Value PT. Onasis Indonesia',
        'app_css': 'about/css/styles.css',
    }
    return render(request, 'about/vision-mission.html', context)
