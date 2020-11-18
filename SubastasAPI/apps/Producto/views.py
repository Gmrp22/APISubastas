from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from .models import Producto
from .serializers import ProductoSerializer, ProductoSerializerUpdate, ProductoSerializerCreate
from rest_framework import status
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)


class ListaProductos(ListAPIView):
    """ Lista todos los productos """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class ProductoPost(CreateAPIView):
    """ Crea un producto """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializerCreate
    permission_classes = [IsAuthenticated, IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(Vendedor=self.request.user)


class ProductoPut(RetrieveUpdateAPIView):
    """ Actualizar producto"""
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializerUpdate
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated, IsAdminUser, IsOwnerOrReadOnly]


class ProductoDelete(RetrieveDestroyAPIView):
    """ Eliminar un producto """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated, IsAdminUser, IsOwnerOrReadOnly]
