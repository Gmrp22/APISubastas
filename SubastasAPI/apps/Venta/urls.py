from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    #path('Subastas/', .as_view()),
    path('Ventas/', ListaVentas.as_view()),
    path('Ventas/POST/', VentaPost.as_view()),
    path('Ventas/PUT/<int:pk>/', VentaPut.as_view()),
    
]
