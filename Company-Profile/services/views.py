from urllib import request
from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': 'Product & Services',
        'heading': 'Welcome to Product & Services',
        'app_css': 'about/css/styles.css',
    }
    return render(request, 'services/index.html', context)
