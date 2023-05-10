from django import forms
from app_creditos.models import Clientes, Tipo_Credito, Creditos


   
class CreditoFormulario(forms.Form):
    cliente = forms.ModelChoiceField(queryset=Clientes.objects.all())
    tipo_credito = forms.ModelChoiceField(queryset=Tipo_Credito.objects.all())
    monto = forms.IntegerField(required=True)
    cuotas = forms.IntegerField(required=True)
    monto_cuota = forms.IntegerField()

