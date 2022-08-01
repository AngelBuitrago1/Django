from django.shortcuts import render
from django.http import HttpResponse
from udemyApp.models import Webs, Temas
from . import forms

def vista1(request):
    return HttpResponse("Hola conocimiento")

def vista2(request):
    return HttpResponse("aprendiendo a crear endponits en archivos ubicados dentro del proyecto")

def vista3(request):
    diccionario = {'etiqueta':'Valor de la etiqueta'}
    return render(request,"pagina1.html", context=diccionario)
    # (request,"carpeta/pagina1.html", context=diccionario) en caso que se agrupen los template por app

def vista4(request):
    diccionario = {}
    return render(request,"pagina2.html", context=diccionario)

def vista5(request):
    lista_webs = Webs.objects.order_by('nombre')
    diccionario = {'lista_webs':lista_webs}
    return render(request, "portada.html", context=diccionario)

def vista6(request):
    formulario = forms.Formulario()
    diccionario = {'formulario':formulario}

    if request.method =='POST':
        formulario1 = forms.Formulario(request.POST)
        if formulario1.is_valid():
            nombre = formulario1.cleaned_data['nombre']
            email = formulario1.cleaned_data['email']
            print("Nombre = "+nombre)
            print("Correo electrónico = "+email)
    return render(request, "pagina3.html", context=diccionario)

def pagina4(request):
    diccionario = {}
    return render(request,"pagina4.html", context=diccionario)

def pagina5(request):
    diccionario = {"texto":"uso filtros", "cantidad":1000, "fecha":"30/07/2022"}
    return render(request,"pagina5.html", context=diccionario)

def plantilla(request):
    diccionario = {}
    return render(request, "plantilla.html", context=diccionario)

def ejercicio(request):
    diccionario = {'etiqueta':'Este es el reultado del ejercicio'}
    return render(request, "ejercicio1.html", context=diccionario)

def ejercicio2(request):
    lista_webs = Webs.objects.order_by('nombre')
    lista_temas = Temas.objects.all()
    diccionario = {'lista_webs':lista_webs, 'lista_temas':lista_temas}
    return render(request, "portada1.html", context=diccionario)