from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from .models import Producto
from .serializers import ProductoSerializer
from rest_framework import status
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
# Create your views here.


class ListaProductos(ListAPIView):
    """ Lista todos los productos """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class ProductoPost(CreateAPIView):
    """ Crea un producto """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated,IsAdminUser]

    def perform_create(self,serializer):
        """Metodo para relacionar solo con usuario creador"""
        serializer.save(user= self.request.user)

class ProductoPut(RetrieveUpdateAPIView):
    """ Actualizar producto"""
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated,IsAdminUser]

    def perform_update(self,serializer):
        """Metodo para relacionar solo con usuario creador"""
        serializer.save(user= self.request.user)


class ProductoDelete(RetrieveDestroyAPIView):
    """ Eliminar un producto """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    lookup_field = 'pk'
