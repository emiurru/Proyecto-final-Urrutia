from django.shortcuts import render

def html(request):
    contexto = {}
    http_responde = render(
        request=request,
        template_name='app_creditos/base.html',
        context=contexto
    )
    return http_responde