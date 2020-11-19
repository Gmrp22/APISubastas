from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('Usuarios/', UserList.as_view()),
    path('Usuarios/<int:pk>/', UserDetail.as_view()),

]
