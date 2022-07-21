from enum import unique
from pyexpat import model
from django.db import models


class Categoria(models.Model):
    """Modelo para tabla de categorias"""


    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    nombre_categoria = models.CharField("Categoria", max_length=60,unique=True)


    def __str__(self):
        return str(self.id) +  '-' +   self.nombre_categoria 


class Subcategoria(models.Model):
    nombre_subcategoria = models.CharField("Subategoria", max_length=60)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,)

    def __str__(self):
        return str(self.id) +  '-' +   self.nombre_subcategoria 
        
    """Modelo para tabla de Sub categorias"""

  
    
