# Generated by Django 4.0.5 on 2022-06-17 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busqueda', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='busqueda',
            name='ubicacion',
        ),
        migrations.AlterField(
            model_name='busqueda',
            name='ciudad',
            field=models.CharField(max_length=255, verbose_name='Zona/Barrio del partido'),
        ),
    ]
