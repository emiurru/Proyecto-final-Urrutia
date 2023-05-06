from django import forms
from app_creditos.models import Clientes, Tipo_Credito, Creditos


class ClientesFormulario(forms.Form):
    apellido = forms.CharField(required=True, max_length=64)
    nombre = forms.CharField(required=True, max_length=64) 
    dni = forms.IntegerField(required=True)
    email = forms.EmailField(required=True)

class Tipo_Credito_Formulario(forms.Form):
    nombre_credito = forms.CharField(required=True, max_length=64) 
    interes = forms.FloatField(required=True)
    
class CreditoFormulario(forms.Form):
    cliente = forms.ModelChoiceField(queryset=Clientes.objects.all())
    tipo_credito = forms.ModelChoiceField(queryset=Tipo_Credito.objects.all())
    monto = forms.IntegerField(required=True)
    cuotas = forms.IntegerField(required=True)
    monto_cuota = forms.IntegerField()

