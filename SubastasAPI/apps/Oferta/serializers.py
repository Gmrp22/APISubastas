from rest_framework.serializers import ModelSerializer
from .models import Oferta


class OfertaSerializer(ModelSerializer):
    """Serializer para oferta """
    class Meta:
        model = Oferta
        fields = ['id', 'Precio', 'Subasta']
