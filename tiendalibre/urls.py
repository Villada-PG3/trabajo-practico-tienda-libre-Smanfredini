from django.urls import path
from . import views 
from .views import HomeView, CatalogoView, DetailView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("home/", HomeView.as_view(), name="home"),
    path("catalogo/", CatalogoView.as_view(), name="catalogo"),
    path("productos/", views.productos, name="productos"),
    path("acerca_de_mi/", views.Acerca_De_Mi, name="acerca_de_mi"),
    path("producto/<int:pk>/", DetailView.as_view(), name="detalle_producto"),
]
