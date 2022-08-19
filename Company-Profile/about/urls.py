from django.urls import path

from . import views

urlpatterns = [
    path('orchart/', views.orchart, name='orchart'),
    path('visionmission/', views.visionMission, name='visionmission'),
    path('', views.index, name='index'),
]
