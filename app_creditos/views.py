from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from app_creditos.models import Clientes, Tipo_Credito, Creditos
from .utils import calcular_descuento_cheque
from datetime import datetime
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from decimal import Decimal

# VISTAS CLIENTES
class ClientesListView(ListView):
    model = Clientes
    template_name = 'app_creditos/lista_clientes.html'

class ClientesCreateView(CreateView):
    model = Clientes
    fields = ('apellido', 'nombre', 'dni', 'email')
    success_url = reverse_lazy('lista_clientes')

class ClientesDetailView(DetailView):
    model = Clientes
    success_url = reverse_lazy('lista_clientes')

class ClientesUpdateView(UpdateView):
    model = Clientes
    fields = ('apellido', 'nombre', 'dni', 'email')
    success_url = reverse_lazy('lista_clientes')

class ClientesDeleteView(DeleteView):
    model = Clientes
    success_url = reverse_lazy('lista_clientes')

# VISTAS TIPOS DE CREDITOS
class Tipo_creditoListView(ListView):
    model = Tipo_Credito
    template_name = 'app_creditos/lista_tipo_creditos.html'

class Tipo_creditoCreateView(CreateView):
    model = Tipo_Credito
    fields = ('nombre_credito', 'interes')
    success_url = reverse_lazy('lista_tipo_creditos')

class Tipo_creditoDetailView(DetailView):
    model = Tipo_Credito
    success_url = reverse_lazy('lista_tipo_creditos')

class Tipo_creditoUpdateView(UpdateView):
    model = Tipo_Credito
    fields = ('nombre_credito', 'interes')
    success_url = reverse_lazy('lista_tipo_creditos')

class Tipo_creditoDeleteView(DeleteView):
    model = Tipo_Credito
    success_url = reverse_lazy('lista_tipo_creditos')

#VISTAS DE CREDITOS
class CreditosListView(ListView):
    model = Creditos
    template_name = 'app_creditos/lista_creditos.html'

class CreditosCreateView(CreateView):
    model = Creditos
    fields = ('monto', 'cuotas', 'cliente', 'tipo_credito')
    success_url = reverse_lazy('lista_creditos')

class CreditosDetailView(DetailView):
    model = Creditos
    success_url = reverse_lazy('lista_creditos')

class CreditosUpdateView(UpdateView):
    model = Creditos
    fields = ('monto', 'cuotas', 'tipo_credito')
    success_url = reverse_lazy('lista_creditos')

class CreditosDeleteView(DeleteView):
    model = Creditos
    success_url = reverse_lazy('lista_creditos')




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

