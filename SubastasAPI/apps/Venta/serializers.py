from rest_framework.serializers import ModelSerializer
from .models import Venta
class VentaSerializer(ModelSerializer):
    """ Serializer para ventas"""
    class Meta:
        model = Venta
        fields = ['id','Vendedor','Total', 'Subasta', 'Promedio']

class VentaSerializerCreate(ModelSerializer):
    """ Serializer para crear ventas"""
    class Meta:
        model = Venta
        fields = ['Subasta']

class VentaSerializerUpdate(ModelSerializer):
    """ Serializer para actualizar venta
    Se usa tambien para procesar venta, si se selecciona un total, se termina la venta
    """
    class Meta:
        model = Venta
        fields = ['Total', 'Subasta', 'Promedio']