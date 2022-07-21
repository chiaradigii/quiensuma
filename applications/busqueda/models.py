from django.db import models
from location_field.models.plain import PlainLocationField
from ckeditor.fields import RichTextField
from applications.categoria.models import Categoria, Subcategoria
from datetime import date



class RolPlantilla(models.Model):
    rol = models.CharField("Ron en plantilla", max_length=40,)
        
    def __str__(self):
        return str(self.id) +  '-' +   self.rol



class Busqueda(models.Model):
    """Modelo para tabla Busqueda de jugadores"""
    
    TIPOCANCHA_CHOICES = (
    ('0', '5 vs 5'),
    ('1','7 vs 7'),
    ('2','9 vs 9'),
    ('2','11 vs 11'),
    )
    TIPOSUELO_CHOICES = (
    ('0', 'Pasto'),
    ('1','Sintético'),
    ('2','Piso'), 
    )

   
    jugadoresQueFaltan = models.IntegerField("Le faltan",null=True)
    rol = models.ForeignKey(RolPlantilla,on_delete=models.CASCADE,)
    posicion = models.ManyToManyField(Subcategoria)
    tipo_cancha =  models.CharField("Tipo de cancha",max_length=50,choices=TIPOCANCHA_CHOICES,blank=True,)
    tipo_suelo =  models.CharField("Tipo de suelo",max_length=50,choices=TIPOSUELO_CHOICES,blank=True,default='Pasto')
    remera_propia = models.BooleanField(default=False,)
    ciudad = models.CharField("Zona/Barrio del partido",max_length=255)
    # ubicacion = PlainLocationField(based_fields=['ciudad'], zoom=7)
    descripcion = RichTextField(blank=True,)
    fecha = models.DateTimeField("Fecha del partido", auto_now=False, auto_now_add=False,null=True)
    class Meta:
        verbose_name = 'Busqueda'
        verbose_name_plural = 'Busquedas'
        ordering = ['fecha'] #ordena por fecha

    def __str__(self):
        return str(self.id) +  '-' + str(self.ciudad)  + '-' + str(self.posicion)

