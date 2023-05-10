from django.contrib import admin
from django.urls import path

from app_creditos.views import listar_clientes, listar_tipo_creditos, listar_creditos, crear_clientes, crear_tipo_credito, crear_credito,\
      buscar_clientes, buscar_tipo_creditos, buscar_creditos, cotizar_cheque, resultado_cotizacion, eliminar_tipo_credito, editar_tipo_credito

urlpatterns = [
    path("lista-clientes/", listar_clientes, name="lista-clientes"),
    path('tipo-creditos/', listar_tipo_creditos, name='lista-tipo-creditos'),
    path('creditos/', listar_creditos, name='lista-creditos'),
    path('crear-clientes/', crear_clientes, name='crear-clientes'),
    path('crear-tipo-credito/', crear_tipo_credito, name='crear-tipo-credito'),
    path('crear-credito/', crear_credito, name='crear-credito'),
    path('buscar-clientes/', buscar_clientes, name='buscar-clientes'),
    path('buscar-tipo-creditos/', buscar_tipo_creditos, name='buscar-tipo-creditos'),
    path('buscar-creditos/', buscar_creditos, name='buscar-creditos'),
    path('buscar-creditos/', buscar_creditos, name='buscar-creditos'),
    path('formulario-cotizacion/', cotizar_cheque, name='cotizar-cheque'),
    path('resultado-cotizacion/', resultado_cotizacion, name='resultado-cotizacion'),
    path('eliminar-tipo-credito/<int:id>/', eliminar_tipo_credito, name="eliminar-tipo-credito"),
    path('editar-tipo-credito/<int:id>/', editar_tipo_credito, name="editar-tipo-credito"),
    
] 