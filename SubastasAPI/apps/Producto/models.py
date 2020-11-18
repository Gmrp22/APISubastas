from django.db import models
#from apps.Usuario.models import Usuario
from django.contrib.auth.models import User
# Create your models here.
class Producto(models.Model):
    """ Modelo del producto"""

    Nombre = models.CharField(max_length=200)
    Codigo = models.CharField(max_length=200, default="")
    Estado = models.CharField(max_length=200, default='Espera', blank=True)
    Vendedor = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return '{}'.format(self.id)
