from django.db import models
from apps.Subasta.models import Subasta
from apps.Oferta.models import Oferta
from apps.Producto.models import Producto
# Create your models here.
class Venta(models.Model):
    """ Modelo de venta"""
    Fecha = models.DateField()
    #Vendedor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    #Total = models.OneToOneField(Oferta, on_delete=models.CASCADE)
    #Subasta = models.OneToOneField(Subasta, on_delete=models.CASCADE)
    #Producto = models.OneToOneField(Producto, on_delete=models.CASCADE)