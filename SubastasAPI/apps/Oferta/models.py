from django.db import models
from apps.Subasta.models import Subasta

class Oferta(models.Model):
    """ Modelo para subastas"""
    Precio = models.FloatField()
    Subasta = models.ForeignKey(Subasta, on_delete=models.CASCADE)
    #Usuario_oferta = models.ForeignKey(Usuario, on_delete=models.CASCADE)