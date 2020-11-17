from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('Ofertas/', ListaOfertas.as_view()),
    path('Ofertas/POST', OfertaPost.as_view()),
    path('Ofertas/DELETE/<int:pk>/', OfertaDelete.as_view()),
    path('Ofertas/PUT/<int:pk>/', OfertaPut.as_view()),    #path('Ofertas/', .as_view()),


]
