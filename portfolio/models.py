from django.db import models

# Create your models here.
class Proyecto(models.Model):
    """
    Modelo de los proyectos para el portfolio
    """
    titulo = models.CharField(max_length=50, unique=True, verbose_name='Titulo')
    descipcion = models.TextField(verbose_name='Descripción')
    imagen = models.ImageField(upload_to='proyecto',verbose_name='Imagen')
    link = models.URLField(max_length=250, null=True, blank=True ,verbose_name='URL del proyecto')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    fecha_modificacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        ordering = ['-fecha_creacion']

class Habilidad(models.Model):
    """
    Modelo de las habilidades para el portfolio
    """
    titulo = models.CharField(max_length=50, unique=True, verbose_name='Titulo')
    imagen = models.ImageField(upload_to='habilidad',verbose_name='Imagen')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    fecha_modificacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        ordering = ['-fecha_creacion']