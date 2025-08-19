from django.contrib import admin
from .models import Proyecto

# Register your models here.

class ProyectoAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')
    list_display = ['titulo', 'fecha_creacion', 'fecha_modificacion']

admin.site.register(Proyecto, ProyectoAdmin)
