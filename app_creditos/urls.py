from django.contrib import admin
from django.urls import path

from app_creditos.views import listar_clientes, listar_tipo_creditos, listar_creditos

urlpatterns = [
    path("lista-clientes/", listar_clientes, name="lista-clientes"),
    path('tipo-creditos/', listar_tipo_creditos, name='lista-tipo-creditos'),
    path('creditos/', listar_creditos, name='lista-creditos'),
    
] 