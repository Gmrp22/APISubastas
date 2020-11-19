from rest_framework.serializers import ModelSerializer
from apps.Producto.models import Producto


class ProductoSerializer(ModelSerializer):
    """ Serializer para listar"""
    class Meta:
        model = Producto
        fields = ['id', 'Nombre', 'Codigo', 'Estado', 'Vendedor']


class ProductoSerializerUpdate(ModelSerializer):
    """ Serializer para updte"""
    class Meta:
        model = Producto
        fields = ['id', 'Nombre', 'Codigo']


class ProductoSerializerCreate(ModelSerializer):
    """Serializer para create """
    class Meta:
        model = Producto
        fields = ['id', 'Nombre', 'Codigo']
