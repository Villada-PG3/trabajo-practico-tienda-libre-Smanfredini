from django.http import HttpResponse
from django.shortcuts import render
from .models import Producto

def productos(request):
    lista_productos = Producto.objects.all()

    contexto = {
        "productos": lista_productos
    }

    return render(request, "tiendalibre/productos.html", contexto)


def home(request):
    return render(request, "tiendalibre/home.html")

def Acerca_De_Mi(request):
    return render(request, "tiendalibre/acerca_de_mi.html")