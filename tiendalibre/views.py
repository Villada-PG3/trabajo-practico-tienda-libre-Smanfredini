from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView
from .models import Producto, Categoria
from django.db.models import Q
from .forms import ContactoForm

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

    def get_queryset(self):
        queryset = Producto.objects.all()
        busqueda = self.request.GET.get("q", "")
        if busqueda:
            queryset = queryset.filter(
                Q(nombre__icontains=busqueda)
                | Q(marca__icontains=busqueda)
                | Q(descripcion__icontains=busqueda))
        return queryset

class CategoriaView(ListView):
    model = Producto
    template_name = "tiendalibre/categoria.html"
    context_object_name = "productos"
    paginate_by = 6

    def get_queryset(self):
        return Producto.objects.filter(
            categoria__slug=self.kwargs["slug"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["categoria"] = get_object_or_404(
            Categoria,
            slug=self.kwargs["slug"])
        return context

def contacto(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)

        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            email = form.cleaned_data["email"]
            asunto = form.cleaned_data["asunto"]
            mensaje = form.cleaned_data["mensaje"]
            telefono = form.cleaned_data["telefono"]

            return render(request, "tiendalibre/contacto.html", {
                "form": ContactoForm(),
                "exito": True
            })

    else:
        form = ContactoForm()

    return render(request, "tiendalibre/contacto.html", {
        "form": form
    })