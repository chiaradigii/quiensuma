from django.db import models
from ckeditor.fields import RichTextField

from applications.categoria.models import Categoria, Subcategoria
from datetime import date

from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver

class Jugador(models.Model):
    SEXO_CHOICES = (
    ('0', 'Femenino'),
    ('1','Masculino'),
    )
    PIEHABIL_CHOICES = (
    ('0', 'Derecho'),
    ('1','Izquierdo'),
    ('2','Indistinto')
    )
    PROVINCIAS_CHOICES = (
    ('0', 'Buenos Aires'),
    ('1','Cordoba'),
    ('2','Rosario'),
    )
   
    """Modelo para tabla Jugador"""
    
    nombre = models.CharField("nombres", max_length=30,)
    apellido = models.CharField("apellidos", max_length=60)
    fecha_nacimiento = models.DateField("fecha de nacimiento", auto_now=False, auto_now_add=False)
    categoria = models.ManyToManyField(Subcategoria)
    sexo =  models.CharField("sexo",max_length=50,choices=SEXO_CHOICES)
    correo = models.EmailField(max_length=254, unique=True) #email unico 
    descripcion = RichTextField(blank=True,)
    #info de direccion
    provincia =  models.CharField("provincia",max_length=50,choices=PROVINCIAS_CHOICES,default="Buenos Aires")
    localidad = models.CharField("localidad", max_length=100,default="vacio")
    imagen = models.ImageField(upload_to='jugador', blank=True,)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Jugador'
        verbose_name_plural = 'Jugadores'
        ordering = ['nombre'] #ordena por nombre
        unique_together = ('nombre','apellido')#no permite que la combinacion de estos se repita en la BD


    def calcular_años(self):
        today = date.today()
        return today.year - self.fecha_nacimiento.year - ((today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))

    def __str__(self):
        return str(self.id) +  '-' +   self.nombre +  '-' + self.apellido 

# @receiver(post_save, sender=User)
# def update_user_jugador(sender, instance, created, **kwargs):
#     if created:
#         Jugador.objects.create(user=instance)
#     instance.profile.save()






