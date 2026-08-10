from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("productos/", views.productos, name="productos"),
    path("acerca_de_mi/", views.Acerca_De_Mi, name="acerca_de_mi"),
]
