from rest_framework.serializers import ModelSerializer
from apps.Producto.models import Producto


class ProductoSerializer(ModelSerializer):
    """ Serializer para listar productos"""
    class Meta:
        model = Producto
        fields = ['id', 'Nombre', 'Codigo', 'Estado', 'Vendedor']


class ProductoSerializerUpdate(ModelSerializer):
    """ Serializer para actualizar productos"""
    class Meta:
        model = Producto
        fields = ['id', 'Nombre', 'Codigo']


class ProductoSerializerCreate(ModelSerializer):
    """Serializer para crear productos """
    class Meta:
        model = Producto
        fields = ['id', 'Nombre', 'Codigo']
