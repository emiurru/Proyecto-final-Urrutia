from django.shortcuts import render
from app_creditos.models import Clientes, Tipo_Credito, Creditos

def html(request):
    contexto = {}
    http_responde = render(
        request=request,
        template_name='app_creditos/base.html',
        context=contexto
    )

def listar_clientes(request):
    contexto = {
        'clientes': Clientes.objects.all(),
    }
    
    http_response = render(
        request=request,
        template_name='app_creditos/lista_clientes.html',
        context=contexto,
    )
    return http_response

def listar_tipo_creditos(request):
    contexto = {
        'tipo_creditos': Tipo_Credito.objects.all(),
    }
    
    http_response = render(
        request=request,
        template_name='app_creditos/tipo_creditos.html',
        context=contexto,
    )
    return http_response

def listar_creditos(request):
    contexto = {
        'creditos': Tipo_Credito.objects.all(),
    }
    
    http_response = render(
        request=request,
        template_name='app_creditos/creditos.html',
        context=contexto,
    )
    return http_response