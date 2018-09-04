from django.db import models


# Create your models here.

class Propietario(models.Model):
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    edad = models.IntegerField()
    identificacion = models.CharField(max_length=15)
    email = models.EmailField()
    telefono = models.CharField(max_length=12)

    def __str__(self):
        return '{}'.format(self.nombre)