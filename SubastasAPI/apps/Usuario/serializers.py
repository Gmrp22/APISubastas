from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from apps.Producto.models import Producto
from django.contrib.auth import password_validation, authenticate
from rest_framework.validators import UniqueValidator


class UserSerializer(ModelSerializer):
    """ Serializer para listar usuarios"""
    class Meta:
        model = User
        fields = ['id', 'username', 'is_staff']


class UserSerializerLogIn(ModelSerializer):
    """ Serializer para LogIn"""
    class Meta:
        model = User
        fields = ['id', 'username', 'password']


class UserSerializerSignUp(serializers.Serializer):
    """ Serializer para SignUp"""
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=4, max_length=64)
    is_staff = serializers.BooleanField(default=False)

    def create(self, data):
        user = User.objects.create_user(**data)
        return user
