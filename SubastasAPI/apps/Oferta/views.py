from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from .models import Oferta
from .serializers import OfertaSerializer
from rest_framework import status
from .permissions import IsOwnerOrReadOnly, SubastaTerminada
# Create your views here.
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

class ListaOfertas(ListAPIView):
    """ Lista todas las subastas """
    queryset = Oferta.objects.all()
    serializer_class = OfertaSerializer


class OfertaPost(CreateAPIView):
    """ Crea una subasta """
    queryset = Oferta.objects.all()
    serializer_class = OfertaSerializer
    permission_classes = [IsAuthenticated, SubastaTerminada]

#---un perform create que verifique estaado de subasta ----

class OfertaPut(RetrieveUpdateAPIView):
    """ Actualizar subasta"""
    queryset = Oferta.objects.all()
    serializer_class = OfertaSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly, SubastaTerminada]

class OfertaDelete(RetrieveDestroyAPIView):
    """ Eliminar una subasta """
    queryset = Oferta.objects.all()
    serializer_class = OfertaSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
