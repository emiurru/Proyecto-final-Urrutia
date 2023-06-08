from django.test import TestCase

from .models import Clientes, Tipo_Credito

class ClienteTest(TestCase):
    
    def test_creacion_cliente(self):
        cliente = Clientes(apellido='Fernandez', nombre='Juliana', dni='35865423', email='juliana@prueba.com', creador='', user='')
        cliente.save()

        self.assertEqual(Clientes.objects.count(), 1)
        self.assertEqual(cliente.apellido, "Fernandez")
        self.assertEqual(cliente.dni, '35865423')

    def test_creacion_tipo_credito(self):
        tipo_credito= Tipo_Credito(nombre_credito='Prendario', interes=1.4)
        tipo_credito.save()

        self.assertEqual(Tipo_Credito.objects.count(), 1)
        self.assertEqual(tipo_credito.nombre_credito, "Prendario")
        self.assertEqual(tipo_credito.interes, 1.4)