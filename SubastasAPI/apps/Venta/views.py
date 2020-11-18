from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from apps.Subasta.models import Subasta
from .models import Venta
from apps.Oferta.models import Oferta
from apps.Producto.models import Producto
from .serializers import VentaSerializer, VentaSerializerCreate, VentaSerializerUpdate
from rest_framework import status
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from django.db.models import Avg
from .permissions import IsOwnerOrReadOnly, IsOwnerOrReadOnlyCreate
from rest_framework import status


class ListaVentas(ListAPIView):
    """ Lista todas las subastas """
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]  # ---


class VentaPost(CreateAPIView):
    """ Crea una subasta """
    queryset = Venta.objects.all()
    serializer_class = VentaSerializerCreate
    permission_classes = [IsAuthenticated,IsAdminUser, IsOwnerOrReadOnlyCreate]


    def perform_create(self, serializer):
        """Verifica que la venta la realice el dueño del producto"""
        subasta = serializer.validated_data['Subasta']
        dueño = subasta.Nombre_Producto.Vendedor
        if dueño == self.request.user:
            serializer.save(Vendedor=self.request.user)


class VentaPut(RetrieveUpdateAPIView):
    """ Actualizar subasta"""
    queryset = Venta.objects.all()
    serializer_class = VentaSerializerUpdate
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated, IsAdminUser, IsOwnerOrReadOnly]

    """
    Metodo para verificar si se termino la venta
    Si se termino actualiza estado de subasta, el estado de producto y calcula el promedio
    """

    def perform_update(self, serializer):
        instance = serializer.save()
        if instance.Total != None:
            subasta = serializer.data['Subasta']
            promedio = subasta
            subasta = Subasta.objects.get(pk=subasta)
            subasta.Estado = 'Terminado'
            subasta.Precio_Final = serializer.data['Total']
            subasta.save()
            producto = subasta.Nombre_Producto
            producto = Producto.objects.get(id=producto.id)
            producto.Estado = 'Vendido'
            producto.save()
            promedio = Oferta.objects.filter(Subasta=promedio)
            promedio = promedio.aggregate(Avg('Precio'))
            promedio = promedio['Precio__avg']
            serializer.validated_data['Promedio'] = promedio
            instance = serializer.update(instance, serializer.validated_data)
