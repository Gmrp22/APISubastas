from rest_framework.serializers import ModelSerializer
from .models import Venta
class VentaSerializer(ModelSerializer):
    class Meta:
        model = Venta
        fields = ['id','Vendedor','Total', 'Subasta', 'Promedio']

class VentaSerializerCreate(ModelSerializer):
    class Meta:
        model = Venta
        fields = ['Subasta']

class VentaSerializerUpdate(ModelSerializer):
    class Meta:
        model = Venta
        fields = ['Total', 'Subasta', 'Promedio']