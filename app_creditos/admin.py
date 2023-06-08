from django.contrib import admin

from .models import Clientes, Tipo_Credito, Credito

admin.site.register(Clientes)
admin.site.register(Tipo_Credito)
admin.site.register(Credito)
