from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('Subastas/', ListaSubastas.as_view()),
    path('Subastas/POST', SubastaPost.as_view()),
    path('Subastas/DELETE/<int:pk>', SubastaDelete.as_view()),
    path('Subastas/PUT/<int:pk>', SubastaPut.as_view()),

]
