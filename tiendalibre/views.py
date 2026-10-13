from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView
from .models import Producto

def productos(request):
    lista_productos = Producto.objects.all()
    contexto = {"productos": lista_productos}

    return render(request, "tiendalibre/productos.html", contexto)

def Acerca_De_Mi(request):
    return render(request, "tiendalibre/acerca_de_mi.html")

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, "tiendalibre/detalle.html", {"producto": producto})

class HomeView(TemplateView):
    template_name = "tiendalibre/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["productos_recientes"] = Producto.objects.order_by("id")[:6]

        return context


class CatalogoView(ListView):
    model = Producto
    template_name = "tiendalibre/catalogo.html"
    context_object_name = "productos"