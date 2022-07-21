# Generated by Django 4.0.5 on 2022-06-17 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busqueda', '0002_remove_busqueda_ubicacion_alter_busqueda_ciudad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busqueda',
            name='fecha',
            field=models.DateTimeField(null=True, verbose_name='Fecha del partido'),
        ),
        migrations.AlterField(
            model_name='busqueda',
            name='tipo_suelo',
            field=models.CharField(blank=True, choices=[('0', 'Pasto'), ('1', 'Sintético'), ('2', 'Piso')], default='Pasto', max_length=50, verbose_name='Tipo de suelo'),
        ),
    ]