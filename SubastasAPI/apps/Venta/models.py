from django.db import models
from apps.Subasta.models import Subasta
from apps.Oferta.models import Oferta
from apps.Producto.models import Producto
from django.contrib.auth.models import User
# Create your models here.
class Venta(models.Model):
    """ Modelo de venta"""
    Vendedor = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)
    Total = models.OneToOneField(Oferta, on_delete=models.CASCADE, blank=True,   null=True)
    Subasta = models.OneToOneField(Subasta, on_delete=models.CASCADE, blank=False, null=True)
    Promedio = models.FloatField(blank=True, default=0)

    def __str__(self):
        return '{}'.format(self.id)