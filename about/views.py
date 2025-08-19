from django.shortcuts import render
from .models import Curso, Habilidades

# Create your views here.
def about(request):
    """
    Render al HTML de about
    """
    cursos = Curso.objects.all()
    habilidades = Habilidades.objects.all().order_by('fecha_creacion')
    imagen_de_fondo_ccs = 'about'
    active_nav = 'about'
    # print(habilidades)
    contexto = {
        'imagen_ccs': imagen_de_fondo_ccs,
        'active_nav': active_nav, 
        'cursos' : cursos,
        'habilidades' : habilidades
    }
    return render(request, 'about/about.html', contexto)