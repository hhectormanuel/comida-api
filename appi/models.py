from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    precio = models.CharField(max_length=30)
    img = models.CharField(max_length=700)

    def __str__(self):
        return self.nombre

class Orden(models.Model):
    productos = models.ManyToManyField(Producto)