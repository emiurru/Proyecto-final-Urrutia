from django.contrib import admin
from django.urls import path

from app_creditos.views import cotizar_cheque, resultado_cotizacion,\
      ClientesListView, ClientesCreateView, ClientesDetailView, ClientesUpdateView, ClientesDeleteView, Tipo_creditoCreateView,\
      Tipo_creditoListView, Tipo_creditoUpdateView, Tipo_creditoDeleteView, Tipo_creditoDetailView, CreditoListView,\
      CreditoDeleteView, CreditoCreateView, CreditoDetailView, CreditoUpdateView

urlpatterns = [
    #URL Clientes
    path("clientes/", ClientesListView.as_view(), name="lista_clientes"),
    path('crear-clientes/', ClientesCreateView.as_view(), name="crear_clientes"),
    path('clientes/<int:pk>/', ClientesDetailView.as_view(), name="ver_clientes"),
    path('editar-clientes/<int:pk>/', ClientesUpdateView.as_view(), name="editar_clientes"),
    path('eliminar-clientes/<int:pk>/', ClientesDeleteView.as_view(), name="eliminar_clientes"),
    
    #URLs tipos de credito
    path('tipo-creditos/', Tipo_creditoListView.as_view(), name='lista_tipo_creditos'),
    path('crear-tipo-creditos/', Tipo_creditoCreateView.as_view(), name='crear_tipo_creditos'),
    path('tipo-creditos/<int:pk>/', Tipo_creditoDetailView.as_view(), name="ver_tipo_creditos"),
    path('editar-tipo-creditos/<int:pk>/', Tipo_creditoUpdateView.as_view(), name="editar_tipo_creditos"),
    path('eliminar-tipo-creditos/<int:pk>/', Tipo_creditoDeleteView.as_view(), name="eliminar_tipo_creditos"),
       
    #URLs creditos
    path('creditos/', CreditoListView.as_view(), name='lista_creditos'),
    path('crear-creditos/', CreditoCreateView.as_view(), name='crear_creditos'),
    path('creditos/<int:pk>/', CreditoDetailView.as_view(), name="ver_creditos"),
    path('editar-creditos/<int:pk>/', CreditoUpdateView.as_view(), name="editar_creditos"),
    path('eliminar-creditos/<int:pk>/', CreditoDeleteView.as_view(), name="eliminar_creditos"),
    
    #URLs cotizacion cheques
    path('formulario-cotizacion/', cotizar_cheque, name='cotizar-cheque'),
    path('resultado-cotizacion/', resultado_cotizacion, name='resultado-cotizacion'),
    
        
] 