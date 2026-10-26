from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView
from .models import Producto

def productos(request):
    lista_productos = Producto.objects.all()
    contexto = {"productos": lista_productos}

    return render(request, "tiendalibre/productos.html", contexto)

def Acerca_De_Mi(request):
    return render(request, "tiendalibre/acerca_de_mi.html")

class DetailView(DetailView):
    model = Producto
    template_name = "tiendalibre/detalle_producto.html"
    context_object_name = "producto"

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
    paginate_by = 6