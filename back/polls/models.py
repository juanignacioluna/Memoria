from django.db import models

class tablaDeResultados(models.Model):
    nombre = models.CharField(max_length=200)
    mejorPuntaje = models.IntegerField()
    ultimoPuntaje = models.IntegerField()
