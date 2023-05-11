from django.db import models

class Clientes(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    dni = models.CharField(max_length=32)
    email = models.EmailField()

    def __str__(self) -> str:
        return f'{self.apellido}  {self.nombre}'

class Tipo_Credito(models.Model):
    nombre_credito = models.CharField(max_length=256)
    interes = models.FloatField()

    def __str__(self) -> str:
        return f'{self.nombre_credito}. Tasa de interes = {self.interes*100}%'

class Creditos(models.Model):
    monto = models.IntegerField()
    cuotas = models.IntegerField()
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    #monto_cuota = models.IntegerField()
    monto_cuota = models.IntegerField(null=True, blank=True)
    tipo_credito = models.ForeignKey(Tipo_Credito, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.id} - {self.cliente} - Monto: {self.monto} - Cuotas: {self.cuotas}'
    
    def save(self, *args, **kwargs):
        # calcular el valor de monto_cuota antes de guardar
        tasa_interes = self.tipo_credito.interes
        monto = self.monto
        cuotas = self.cuotas
        monto_cuota = (monto * ( 1 + (tasa_interes / 12 * cuotas))) / cuotas
        self.monto_cuota = monto_cuota
        super().save(*args, **kwargs)
    
   