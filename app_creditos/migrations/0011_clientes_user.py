# Generated by Django 4.2.1 on 2023-05-16 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_creditos', '0010_clientes_creador_creditos_creador_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientes',
            name='user',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
