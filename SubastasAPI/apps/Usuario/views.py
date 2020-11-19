from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView,RetrieveAPIView
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerLogIn, UserSerializerSignUp
from rest_framework import status

class UserList(ListAPIView):
    """ Muestra todos los usuarios"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveAPIView):
    """ Muestra un usuario especifico"""
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SignUp(CreateAPIView):
    """ Crea un usuario"""
    queryset = User.objects.all()
    serializer_class = UserSerializerSignUp

