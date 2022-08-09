from django.shortcuts import render

def index(request):
    context = {
        'title': 'Onasis Indonesia',
        'heading': 'Selamat Datang',
        'tag': 'Engineering, Procurement, Construction and Pipeline for Oil & Gas Service',
    }
    return render(request, 'index.html', context)