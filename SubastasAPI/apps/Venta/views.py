from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from apps.Subasta.models import Subasta
from .models import Venta
from .serializers import VentaSerializer, VentaSerializerCreate, VentaSerializerUpdate
from rest_framework import status
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from .permissions import IsOwnerOrReadOnly,IsOwnerOrReadOnlyCreate
from rest_framework import status

class ListaVentas(ListAPIView):
    """ Lista todas las subastas """
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

class VentaPost(CreateAPIView):
    """ Crea una subasta """
    queryset = Venta.objects.all()
    serializer_class = VentaSerializerCreate
    permission_classes = [IsAuthenticated, IsAdminUser, IsOwnerOrReadOnlyCreate]


    def perform_create(self, serializer):
        vendedor = serializer.data['Vendedor']
        if vendedor == self.request.user:
            serializer.save()
        else:
            data = {'message': 'Creacion cancelada, no es el dueño del producto'}
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)



class VentaPut(RetrieveUpdateAPIView):
    """ Actualizar subasta"""
    queryset = Venta.objects.all()
    serializer_class = VentaSerializerUpdate
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated, IsAdminUser, IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        instance = serializer.save()
        if instance.Total != None:
            subasta = serializer.data['Subasta']
            subasta = Subasta.objects.get(pk=subasta)
            subasta.Estado = 'Terminado'
            subasta.Precio= serializer.data['Total']
            subasta.save()
            producto = Subasta.objects.get(Nombre_Producto= subasta.Nombre_Producto)
            producto.Estado = 'Vendido'
            producto.save()
            
