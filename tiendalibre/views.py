from django.http import HttpResponse
from django.shortcuts import render
from .models import Producto

def productos(request):
    lista_productos = Producto.objects.all()

    contexto = {
        "productos": lista_productos
    }

    return render(request, "productos.html", contexto)

def home(request):
    return HttpResponse("<h1>Bienvenido a la tienda en línea</h1>")

def home1(request):
    return render(request, "home.html")