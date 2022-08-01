from django.urls import path
from udemyApp import views

app_name = 'udemyApp'

urlpatterns = [
    path('pagina4/', views.pagina4, name='pagina 4'),
    path('pagina5/', views.pagina5, name='pagina 5'),
    path('plantilla/', views.plantilla, name='plantilla'),
]