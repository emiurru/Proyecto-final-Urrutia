from django.db import models
from datetime import date, datetime, timedelta
from django.contrib.auth.models import User
from .utils import calcular_fecha_vencimiento

class Clientes(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    dni = models.CharField(max_length=32)
    email = models.EmailField()
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f'{self.apellido}  {self.nombre}'

class Tipo_Credito(models.Model):
    nombre_credito = models.CharField(max_length=256)
    interes = models.FloatField()
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f'{self.nombre_credito}. Tasa de interes = {self.interes*100}%'

class Creditos(models.Model):
    monto = models.IntegerField()
    cuotas = models.IntegerField()
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    monto_cuota = models.IntegerField(null=True, blank=True)
    tipo_credito = models.ForeignKey(Tipo_Credito, on_delete=models.CASCADE)
    fecha = models.DateField(null=True, blank=True)
    fecha_otorgamiento = models.DateField(auto_now_add=True, null=True)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    

    def __str__(self) -> str:
        return f'{self.id} - {self.cliente} - Monto: {self.monto} - Cuotas: {self.cuotas}'
    
    def save(self, *args, **kwargs):
        # calcular el valor de monto_cuota antes de guardar
        tasa_interes = self.tipo_credito.interes
        monto = self.monto
        cuotas = self.cuotas
        monto_cuota = (monto * ( 1 + (tasa_interes / 12 * cuotas))) / cuotas
        self.monto_cuota = monto_cuota
        fecha_otorgamiento = date.today()
        super().save(*args, **kwargs)
        
               
        return monto_cuota, fecha_otorgamiento
    
  
 
