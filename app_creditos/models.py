from django.db import models

class Clientes(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    dni = models.CharField(max_length=32)
    email = models.EmailField()

    def __str__(self) -> str:
        return f'{self.apellido}, {self.nombre}'

class Tipo_Credito(models.Model):
    nombre_credito = models.CharField(max_length=256)
    interes = models.FloatField()

    def __str__(self) -> str:
        return f'{self.nombre_credito}. Tasa de interes = {self.interes*100}%'

class Creditos(models.Model):
    monto = models.IntegerField()
    cuotas = models.IntegerField()
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    monto_cuota = models.IntegerField()
    tipo_credito = models.ForeignKey(Tipo_Credito, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.id} - {self.cliente} - Monto: {self.monto} - Cuotas: {self.cuotas}'

        