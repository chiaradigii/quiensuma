# Generated by Django 4.0.5 on 2022-06-17 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busqueda', '0003_alter_busqueda_fecha_alter_busqueda_tipo_suelo'),
    ]

    operations = [
        migrations.AddField(
            model_name='busqueda',
            name='jugadoresQueFaltan',
            field=models.IntegerField(null=True, verbose_name='Le faltan'),
        ),
    ]
