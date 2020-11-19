from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    #path('Subastas/', .as_view()),
    path('Ventas/', ListaVentas.as_view()),
    path('Ventas/POST', VentaPost.as_view()),
    path('Ventas/PUT/<int:pk>', VentaPut.as_view()),
    
    
]

""" Para terminar la venta se hace uso de Ventas/PUT/<int:pk> y se ingresa el total a seleccionar
Este total es una de las ofertas que propuso el cliente
"""