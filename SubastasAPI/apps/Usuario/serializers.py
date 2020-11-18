from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from apps.Producto.models import Producto

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

