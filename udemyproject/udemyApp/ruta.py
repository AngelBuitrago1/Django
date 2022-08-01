from django.urls import path
from udemyApp import views

urlpatterns = [
    path('', views.vista2, name='vista 2'),
]