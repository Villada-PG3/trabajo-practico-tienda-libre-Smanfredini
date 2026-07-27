from django.db import models

# Create your models here.


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    marca = models.CharField(max_length=50, default="Marca Desconocida")

    def __str__(self):
        return f"{self.nombre} - {self.precio} - {self.stock}"