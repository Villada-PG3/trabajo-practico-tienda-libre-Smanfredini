from django.shortcuts import render
from .models import Producto

def productos(request):
    lista_productos = Producto.objects.all()

    contexto = {
        "productos": lista_productos
    }

    return render(request, "productos.html", contexto)