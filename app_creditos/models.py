from django.db import models

class Cliente(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    dni = models.CharField(max_length=32)
    email = models.EmailField()

class Tipo_Credito(models.Model):
    nombre_credito = models.CharField(max_length=64)
    interes = models.FloatField()

class Creditos(models.Model):
    monto = models.IntegerField()
    cuotas = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    monto_cuota = models.IntegerField(max_length=10)

    def calcular_monto_cuota(self):
        interes_mensual = self.tipo_credito.interes / 12
        monto_cuota = (interes_mensual * self.monto) // (1 - (1 + interes_mensual)**(-self.cuotas))
        self.save()
    