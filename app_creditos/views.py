from typing import Any, Dict
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from app_creditos.models import Clientes, Tipo_Credito, Creditos
from .utils import calcular_descuento_cheque
from datetime import datetime, timedelta
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from decimal import Decimal
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# VISTAS CLIENTES

class ClientesListView(LoginRequiredMixin, ListView):
    model = Clientes
    template_name = 'app_creditos/lista_clientes.html'

    def get_queryset(self):
        queryset = super().get_queryset()

        busqueda = self.request.GET.get('busqueda', '')
        queryset = queryset.filter(apellido__icontains=busqueda)
        return queryset

class ClientesCreateView(LoginRequiredMixin, CreateView):
    model = Clientes
    fields = ('apellido', 'nombre', 'dni', 'email')
    success_url = reverse_lazy('lista_clientes')

class ClientesDetailView(LoginRequiredMixin, DetailView):
    model = Clientes
    success_url = reverse_lazy('lista_clientes')

class ClientesUpdateView(LoginRequiredMixin, UpdateView):
    model = Clientes
    fields = ('apellido', 'nombre', 'dni', 'email')
    success_url = reverse_lazy('lista_clientes')

class ClientesDeleteView(LoginRequiredMixin, DeleteView):
    model = Clientes
    success_url = reverse_lazy('lista_clientes')

# VISTAS TIPOS DE CREDITOS
class Tipo_creditoListView(ListView):
    model = Tipo_Credito
    template_name = 'app_creditos/lista_tipo_creditos.html'

    def get_queryset(self):
        queryset = super().get_queryset()

        busqueda = self.request.GET.get('busqueda', '')
        queryset = queryset.filter(nombre_credito__icontains=busqueda)
        return queryset

class Tipo_creditoCreateView(LoginRequiredMixin, CreateView):
    model = Tipo_Credito
    fields = ('nombre_credito', 'interes')
    success_url = reverse_lazy('lista_tipo_creditos')

class Tipo_creditoDetailView(DetailView):
    model = Tipo_Credito
    success_url = reverse_lazy('lista_tipo_creditos')

class Tipo_creditoUpdateView(LoginRequiredMixin, UpdateView):
    model = Tipo_Credito
    fields = ('nombre_credito', 'interes')
    success_url = reverse_lazy('lista_tipo_creditos')

class Tipo_creditoDeleteView(LoginRequiredMixin, DeleteView):
    model = Tipo_Credito
    success_url = reverse_lazy('lista_tipo_creditos')

#VISTAS DE CREDITOS

class CreditosListView(LoginRequiredMixin, ListView):
    model = Creditos
    template_name = 'app_creditos/lista_creditos.html'

    def get_queryset(self):
        queryset = super().get_queryset()

        busqueda = self.request.GET.get('busqueda', '')
        
        if self.request.user.is_superuser:
            queryset = queryset.filter(cliente__apellido__icontains=busqueda)
        else:
            queryset = queryset.filter(cliente__user=self.request.user, cliente__apellido__icontains=busqueda)

        return queryset
     
class CreditosCreateView(LoginRequiredMixin, CreateView):
    model = Creditos
    fields = ('monto', 'cuotas', 'tipo_credito')
    success_url = reverse_lazy('lista_creditos')

    def form_valid(self, form):
        cliente = self.request.user.cliente
        form.instance.cliente = cliente

        return super().form_valid(form)

class CreditosDetailView(LoginRequiredMixin, DetailView):
    model = Creditos
    success_url = reverse_lazy('lista_creditos')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        credito = context['object']
        #context['monto_cuota'] = credito.monto_cuota
        
        numero_cuotas = credito.cuotas
        fecha_otorgamiento = credito.fecha_otorgamiento

        lista_cuotas = []
        for nro_cuota in range(1, numero_cuotas + 1):
            fecha_vencimiento = fecha_otorgamiento + timedelta(days=30 * nro_cuota)
            importe_cuota = credito.monto_cuota
            cuota = {
                'nro_cuota': nro_cuota,
                'fecha_vencimiento': fecha_vencimiento,
                'importe_cuota': importe_cuota,
            }
            lista_cuotas.append(cuota)

        context['cuotas'] = lista_cuotas
        return context
    
class CreditosUpdateView(LoginRequiredMixin, UpdateView):
    model = Creditos
    fields = ('monto', 'cuotas', 'tipo_credito')
    success_url = reverse_lazy('lista_creditos')

class CreditosDeleteView(LoginRequiredMixin, DeleteView):
    model = Creditos
    success_url = reverse_lazy('lista_creditos')


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

