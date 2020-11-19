from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from .models import Subasta
from .serializers import SubastaSerializer, SubastaSerializerCreate
from rest_framework import status
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from .permissions import IsOwnerOrReadOnly, SubastaTerminada
from rest_framework import status


class ListaSubastas(ListAPIView):
    """ Lista todas las subastas """
    queryset = Subasta.objects.all()
    serializer_class = SubastaSerializer
    permission_classes = [IsOwnerOrReadOnly]


class SubastaPost(APIView):
    """ Crea una subasta """
    permission_classes = [IsAuthenticated, IsAdminUser]

    """ 
    Crea la subasta, si no se cumple con los permisos y si no es el dueño del 
    producto no lo permitira 
    """

    def post(self, request, format=None):
        serializer = SubastaSerializerCreate(data=request.data)
        if serializer.is_valid():
            producto = serializer.validated_data['Nombre_Producto']
            dueño = producto.Vendedor
            if dueño == self.request.user:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                contexto = {'Error': 'Usted no es el dueño de este producto'}
                return Response(contexto, status=status.HTTP_403_FORBIDDEN)
        return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)


class SubastaPut(RetrieveUpdateAPIView):
    """ Actualizar subasta"""
    queryset = Subasta.objects.all()
    serializer_class = SubastaSerializerCreate
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated, IsAdminUser,IsOwnerOrReadOnly, SubastaTerminada]


class SubastaDelete(RetrieveDestroyAPIView):
    """ Eliminar una subasta """
    queryset = Subasta.objects.all()
    serializer_class = SubastaSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated, IsAdminUser, IsOwnerOrReadOnly]
