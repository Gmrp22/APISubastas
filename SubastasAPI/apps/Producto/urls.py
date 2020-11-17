from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('Productos/', ListaProductos.as_view()),
    path('Productos/POST', ProductoPost.as_view()),
    path('Productos/DELETE/<int:pk>/', ProductoDelete.as_view()),
    path('Productos/PUT/<int:pk>/', ProductoPut.as_view()),

]
