# Generated by Django 4.2.1 on 2023-06-07 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_creditos', '0002_rename_monto_creditos_importe_credito'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditos',
            name='monto_cuota',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='lista_cuota',
            name='numero_cuota',
            field=models.IntegerField(),
        ),
    ]
