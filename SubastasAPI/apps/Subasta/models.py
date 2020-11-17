from django.db import models
from apps.Producto.models import Producto
# Create your models here.
class Subasta(models.Model):
    """ Modelo para subastas"""
    Nombre_Producto = models.OneToOneField(Producto, on_delete=models.CASCADE, unique = True)    
    Estado = models.CharField(max_length=200, blank =True, default='Espera')
    Precio_Final = models.FloatField(blank=True, default=0)

    def __str__(self):
        return '{}'.format(self.id)