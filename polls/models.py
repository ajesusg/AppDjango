import datetime
from django.db import models
from django.utils import timezone

class Parametro(models.Model):
    voltaje = models.CharField(max_length=200)
    corriente = models.CharField(max_length=200)
    potencia = models.CharField(max_length=200)
    fecha = models.DateTimeField('fecha')
    def __str__(self):
        return self.voltaje
        return self.corriente
