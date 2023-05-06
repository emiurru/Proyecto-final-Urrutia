from django.contrib import admin
from django.urls import path

from app_creditos.views import listar_clientes, listar_tipo_creditos, listar_creditos, crear_clientes, crear_tipo_credito, crear_credito

urlpatterns = [
    path("lista-clientes/", listar_clientes, name="lista-clientes"),
    path('tipo-creditos/', listar_tipo_creditos, name='lista-tipo-creditos'),
    path('creditos/', listar_creditos, name='lista-creditos'),
    path('crear-clientes/', crear_clientes, name='crear-clientes'),
    path('crear-tipo-credito/', crear_tipo_credito, name='crear-tipo-credito'),
    path('crear-credito/', crear_credito, name='crear-credito'),
    
] 