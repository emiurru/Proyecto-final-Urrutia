# Generated by Django 4.2.1 on 2023-05-06 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_creditos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cliente',
            new_name='Clientes',
        ),
        migrations.AlterField(
            model_name='creditos',
            name='monto_cuota',
            field=models.IntegerField(),
        ),
    ]
