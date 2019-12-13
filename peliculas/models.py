from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Pelicula(models.Model):

    nombre = models.CharField(max_length=30, null=False)
    genero = models.CharField(max_length=15, null=True, blank=True)
    duracion = models.IntegerField()
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre


class Renta(models.Model):
    usuario = models.ForeignKey(User, verbose_name='usuario', on_delete=models.CASCADE)
    fecha = models.DateField(null=True, blank=True)

    
class Detalle_Renta(models.Model):
    renta = models.ForeignKey(Renta, verbose_name="Renta", on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, verbose_name="Pelicula", on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
