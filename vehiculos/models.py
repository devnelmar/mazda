from django.db import models
from propietarios.models import Propietario


# Create your models here.

class Vehiculo(models.Model):
    id_propietario = models.ForeignKey(Propietario, null=True, blank=True, on_delete=models.CASCADE)
    placa = models.CharField(max_length=50)
    modelo = models.CharField(max_length=10)
    tipo_vehiculo = models.CharField(max_length=10)

    def __str__(self):
        return '{}'.format(self.modelo)
