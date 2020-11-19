from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from .models import Oferta
from .serializers import OfertaSerializer
from rest_framework import status
from .permissions import IsOwnerOrReadOnly, SubastaTerminada
from rest_framework.views import exception_handler
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


# class OfertaPost(CreateAPIView):
#     """ Crea una subasta """
#     queryset = Oferta.objects.all()
#     serializer_class = OfertaSerializer
#     permission_classes = [IsAuthenticated, SubastaTerminada]

#     def perform_create(self, serializer):
#         """Verificar que la subasta este activa y guarda el usuario que realizo la oferta"""
#         subasta = serializer.validated_data['Subasta']
#         if subasta.Estado == 'Espera':
#             serializer.save(Usuario_oferta=self.request.user)
        
class OfertaPost(APIView):
    permission_classes = [IsAuthenticated, SubastaTerminada]

    def post(self, request, format=None):
        serializer = OfertaSerializer(data=request.data)
        if serializer.is_valid():
            subasta = serializer.validated_data['Subasta']
            if subasta.Estado == 'Espera':
                serializer.save(Usuario_oferta=self.request.user)            
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                contexto = {'Error':'Subasta terminada'}
                return Response(contexto, status=status.HTTP_403_FORBIDDEN)
        return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)



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
