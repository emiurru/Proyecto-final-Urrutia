from django.shortcuts import render, redirect
from django.urls import reverse
from app_creditos.models import Clientes, Tipo_Credito, Creditos
from app_creditos.forms import ClientesFormulario, Tipo_Credito_Formulario, CreditoFormulario
from .utils import calcular_descuento_cheque
from datetime import datetime


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
        tipo_creditos = Tipo_Credito.objects.filter(nombre_credito__icontains=busqueda)
        contexto = {
            "tipo_creditos": tipo_creditos,
        }
        http_response = render(
            request=request,
            template_name='app_creditos/tipo_creditos.html',
            context=contexto,
        )
        return http_response

def buscar_creditos(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        credito = Creditos.objects.filter(cliente__apellido__contains=busqueda)
        contexto = {
            "creditos": credito,
        }
        http_response = render(
            request=request,
            template_name='app_creditos/creditos.html',
            context=contexto,
        )
        return http_response
    
def cotizar_cheque(request):
    if request.method == 'POST':
        monto = float(request.POST.get('monto'))
        tna1 = 120
        tna = tna1 / 100
        fecha_deposito = datetime.strptime(request.POST.get('fecha_deposito'), '%Y-%m-%d').date()

        valor_descontado = calcular_descuento_cheque(monto, tna, fecha_deposito)

        return render(request, 'app_creditos/resultado_cotizacion.html', {'valor_descontado': valor_descontado, 'monto': int(monto), 'tna1': tna1, 'fecha_deposito': fecha_deposito})
    else:
        return render(request, 'app_creditos/formulario_cotizacion.html')
    
def resultado_cotizacion(request):
    return render(request, 'app_creditos/resultado_cotizacion.html')