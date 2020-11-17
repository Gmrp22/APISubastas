from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from .models import Producto
from .serializers import ProductoSerializer
from rest_framework import status
# Create your views here.


class ListaProductos(ListAPIView):
    """ Lista todos los productos """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class ProductoPost(CreateAPIView):
    """ Crea un producto """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class ProductoPut(RetrieveUpdateAPIView):
    """ Actualizar producto"""
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    lookup_field = 'pk'


class ProductoDelete(RetrieveDestroyAPIView):
    """ Eliminar un producto """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    lookup_field = 'pk'
