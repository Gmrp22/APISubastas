from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from .models import Subasta
from .serializers import SubastaSerializer
from rest_framework import status
# Create your views here.


class ListaSubastas(ListAPIView):
    """ Lista todas las subastas """
    queryset = Subasta.objects.all()
    serializer_class = SubastaSerializer


class SubastaPost(CreateAPIView):
    """ Crea una subasta """
    queryset = Subasta.objects.all()
    serializer_class = SubastaSerializer


class SubastaPut(RetrieveUpdateAPIView):
    """ Actualizar subasta"""
    queryset = Subasta.objects.all()
    serializer_class = SubastaSerializer
    lookup_field = 'pk'


class SubastaDelete(RetrieveDestroyAPIView):
    """ Eliminar una subasta """
    queryset = Subasta.objects.all()
    serializer_class = SubastaSerializer
    lookup_field = 'pk'
