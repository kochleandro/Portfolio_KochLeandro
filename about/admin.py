from django.contrib import admin
from .models import Curso, Habilidades

# Register your models here.
class CursoAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')
    list_display = ['titulo', 'fecha_creacion', 'fecha_modificacion']

admin.site.register(Curso, CursoAdmin)

class HabilidadesAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')
    list_display = ['titulo', 'fecha_creacion', 'fecha_modificacion']

admin.site.register(Habilidades, HabilidadesAdmin)