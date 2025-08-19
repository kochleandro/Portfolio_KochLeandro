from django.db import models

# Create your models here.
class Curso(models.Model):
    titulo = models.CharField(max_length=50, unique=True, verbose_name='Titulo')
    institucion = models.CharField(max_length=150, verbose_name='Institución')
    descipcion = models.TextField(verbose_name='Descripción')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    fecha_modificacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        ordering = ['-fecha_creacion']


class Habilidades(models.Model):
    titulo = models.CharField(max_length=50, unique=True, verbose_name='Titulo')
    imagen = models.ImageField(upload_to='about',verbose_name='Imagen')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    fecha_modificacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        ordering = ['-fecha_creacion']