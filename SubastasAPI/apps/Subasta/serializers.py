from rest_framework.serializers import ModelSerializer
from .models import Subasta
class SubastaSerializer(ModelSerializer):
    """ Serializer para subasta"""
    class Meta:
        model = Subasta
        fields = ['id','Nombre_Producto', 'Estado','Precio_Final']

class SubastaSerializerCreate(ModelSerializer):
    """ Serializer para crear subasta"""
    class Meta:
        model = Subasta
        fields = ['id','Nombre_Producto']