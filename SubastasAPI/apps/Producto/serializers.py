from rest_framework.serializers import ModelSerializer
from apps.Producto.models import Producto
class ProductoSerializer(ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id','Nombre','Codigo','Estado']