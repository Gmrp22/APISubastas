from django.db import models
from apps.Subasta.models import Subasta
from django.contrib.auth.models import User
class Oferta(models.Model):
    """ Modelo para subastas"""
    Precio = models.FloatField()
    Subasta = models.ForeignKey(Subasta, on_delete=models.CASCADE, blank=False, null=False)
    Usuario_oferta = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    
    def __str__(self):
        return '{}'.format(self.id)    