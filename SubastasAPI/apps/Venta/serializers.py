from rest_framework.serializers import ModelSerializer
from .models import Venta
class VentaSerializer(ModelSerializer):
    class Meta:
        model = Venta
        fields = ['id','Vendedor','Total', 'Subasta']

class VentaSerializerCreate(ModelSerializer):
    class Meta:
        model = Venta
        fields = ['Vendedor','Subasta']

class VentaSerializerUpdate(ModelSerializer):
    class Meta:
        model = Venta
        fields = ['Total', 'Subasta', 'Promedio']