from django.contrib import admin
from django.urls import path

from app_creditos.views import listar_creditos, crear_credito,\
      buscar_clientes, buscar_tipo_creditos, buscar_creditos, cotizar_cheque, resultado_cotizacion,\
      ClientesListView, ClientesCreateView, ClientesDetailView, ClientesUpdateView, ClientesDeleteView, Tipo_creditoCreateView,\
      Tipo_creditoListView, Tipo_creditoUpdateView, Tipo_creditoDeleteView, Tipo_creditoDetailView

urlpatterns = [
    #URL Clientes
    path("clientes/", ClientesListView.as_view(), name="lista_clientes"),
    path('crear-clientes/', ClientesCreateView.as_view(), name="crear_clientes"),
    path('clientes/<int:pk>/', ClientesDetailView.as_view(), name="ver_clientes"),
    path('editar-clientes/<int:pk>/', ClientesUpdateView.as_view(), name="editar_clientes"),
    path('eliminar-clientes/<int:pk>/', ClientesDeleteView.as_view(), name="eliminar_clientes"),
    path('buscar-clientes/', buscar_clientes, name='buscar-clientes'),

    #URLs tipos de credito
    path('tipo-creditos/', Tipo_creditoListView.as_view(), name='lista_tipo_creditos'),
    path('crear-tipo-creditos/', Tipo_creditoCreateView.as_view(), name='crear_tipo_creditos'),
    path('tipo-creditos/<int:pk>/', Tipo_creditoDetailView.as_view(), name="ver_tipo_creditos"),
    path('editar-tipo-creditos/<int:pk>/', Tipo_creditoUpdateView.as_view(), name="editar_tipo_creditos"),
    path('eliminar-tipo-creditos/<int:pk>/', Tipo_creditoDeleteView.as_view(), name="eliminar_tipo_creditos"),
    path('buscar-tipo-creditos/', buscar_tipo_creditos, name='buscar-tipo-creditos'),
   
    #URLs creditos
    path('creditos/', listar_creditos, name='lista-creditos'),
    path('crear-credito/', crear_credito, name='crear-credito'),  
    path('buscar-creditos/', buscar_creditos, name='buscar-creditos'),
    #URLs cotizacion cheques
    path('formulario-cotizacion/', cotizar_cheque, name='cotizar-cheque'),
    path('resultado-cotizacion/', resultado_cotizacion, name='resultado-cotizacion'),
    
        
] 