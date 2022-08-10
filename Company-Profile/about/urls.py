from django.urls import path

from . import views

urlpatterns = [
    path('visionmission/', views.visionMission, name='visionmission'),
    path('', views.index, name='index'),
]
