from django.shortcuts import render
from django.http import HttpResponse

def html(request):
    contexto = {}
    http_responde = render(
        request=request,
        template_name='app_creditos/base.html',
        context=contexto
    )
    return http_responde

def inicio(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='app_creditos/index.html',
        context=contexto,
    )
    return http_response