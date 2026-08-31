from django.http import HttpResponse
from django.shortcuts import render
from .models import Producto

def productos(request):
    lista_productos = Producto.objects.all()
    contexto = {"productos": lista_productos}

    return render(request, "tiendalibre/productos.html", contexto)

def home(request):
    productos_destacados = [
        {"nombre": "Remera", "precio": 15000,"stock": 10,},
        {"nombre": "Pantalón", "precio": 25000,"stock": 4,},
        {"nombre": "Zapatillas", "precio": 50000,"stock": 8,},
        {"nombre": "Campera", "precio": 70000,"stock": 2,},
        {"nombre": "Gorra", "precio": None ,"stock": 15,},
        { "nombre": "Mochila", "precio": 30000,"stock": 0,}
    ]
    return render(request, "tiendalibre/home.html", {"productos_destacados": productos_destacados})

def Acerca_De_Mi(request):
    return render(request, "tiendalibre/acerca_de_mi.html")