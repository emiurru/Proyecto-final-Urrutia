from django.shortcuts import render, redirect
from django.urls import reverse
from app_creditos.models import Clientes, Tipo_Credito, Creditos
from app_creditos.forms import ClientesFormulario, Tipo_Credito_Formulario, CreditoFormulario

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
        'creditos': Creditos.objects.all(),
    }
    
    http_response = render(
        request=request,
        template_name='app_creditos/creditos.html',
        context=contexto,
    )
    return http_response

def crear_clientes(request):
    if request.method == "POST":
        formulario = ClientesFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            apellido = data["apellido"]
            nombre = data["nombre"]
            dni = data['dni']
            email = data['email']
            cliente = Clientes(apellido=apellido, nombre=nombre, dni=dni, email=email)  # lo crean solo en RAM
            cliente.save()
            cliente_creado = True

            contexto = {'creado_exitosamente': True}
            return render(request, 'app_creditos/formulario_clientes.html', {'cliente_creado': cliente_creado})
    else:
        formulario = ClientesFormulario()
    http_response = render(
        request=request,
        template_name='app_creditos/formulario_clientes.html',
        context={'formulario': formulario}
    )
    return http_response

def crear_tipo_credito(request):
    if request.method == "POST":
        formulario = Tipo_Credito_Formulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            nombre_credito = data["nombre_credito"]
            interes = data["interes"]
            tipo_credito = Tipo_Credito(nombre_credito=nombre_credito, interes=interes)
            tipo_credito.save()
            tipo_credito_creado = True

            contexto = {'creado_exitosamente': True}
            return render(request, 'app_creditos/formulario_tipo_credito.html', {'tipo_credito_creado': tipo_credito_creado})
    else:
        formulario = Tipo_Credito_Formulario()
    http_response = render(
        request=request,
        template_name='app_creditos/formulario_tipo_credito.html',
        context={'formulario': formulario}
    )
    return http_response

def crear_credito(request):
    if request.method == "POST":
        formulario = CreditoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            cliente = data['cliente']
            tipo_credito = data['tipo_credito']
            monto = data["monto"]
            cuotas = data["cuotas"]
            monto_cuota = data['monto_cuota']

            credito = Creditos(cliente=cliente, tipo_credito=tipo_credito, monto=monto, cuotas=cuotas, monto_cuota=monto_cuota)
            credito.save()
            credito_creado = True

            contexto = {'creado_exitosamente': True}
            return render(request, 'app_creditos/formulario_credito.html', {'credito_creado': credito_creado})
    else:
        formulario = CreditoFormulario()
    http_response = render(
        request=request,
        template_name='app_creditos/formulario_credito.html',
        context={'formulario': formulario}
    )
    return http_response

def buscar_clientes(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        clientes = Clientes.objects.filter(dni__contains=busqueda)
        contexto = {
            "clientes": clientes,
        }
        http_response = render(
            request=request,
            template_name='app_creditos/lista_clientes.html',
            context=contexto,
        )
        return http_response
    
def buscar_tipo_creditos(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        tipo_credito = Tipo_Credito.objects.filter(nombre_credito__icontains=busqueda)
        contexto = {
            "tipo_credito": tipo_credito,
        }
        http_response = render(
            request=request,
            template_name='app_creditos/tipo_creditos.html',
            context=contexto,
        )
        return http_response