from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from .models import Subasta
from .serializers import SubastaSerializer
from rest_framework import status
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from apps.Producto.permissions import IsOwnerOrReadOnly


class ListaSubastas(ListAPIView):
    """ Lista todas las subastas """
    queryset = Subasta.objects.all()
    serializer_class = SubastaSerializer

class SubastaPost(CreateAPIView):
    """ Crea una subasta """
    queryset = Subasta.objects.all()
    serializer_class = SubastaSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class SubastaPut(RetrieveUpdateAPIView):
    """ Actualizar subasta"""
    queryset = Subasta.objects.all()
    serializer_class = SubastaSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated, IsAdminUser]


class SubastaDelete(RetrieveDestroyAPIView):
    """ Eliminar una subasta """
    queryset = Subasta.objects.all()
    serializer_class = SubastaSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated, IsAdminUser]
