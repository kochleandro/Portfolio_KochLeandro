from django.shortcuts import render
from portfolio.models import Proyecto, Habilidad

# Create your views here.

def inicio(request):
    """
    Render al html de inicio
    """
    imagen_de_fondo_ccs = 'portfolio'
    active_nav = 'portfolio'
    proyectos = Proyecto.objects.all()
    habilidades = Habilidad.objects.all()
    contexto = {
        'imagen_ccs': imagen_de_fondo_ccs,
        'active_nav': active_nav,
        'proyectos': proyectos,
        'habilidades': habilidades
    }
    return render(request, 'core/home.html', contexto)

def about(request):
    """
    Render al HTML de about
    """
    imagen_de_fondo_ccs = 'about'
    active_nav = 'about'
    contexto = {
        'imagen_ccs': imagen_de_fondo_ccs,
        'active_nav': active_nav
    }
    return render(request, 'core/about.html', contexto)

def contact(request):
    """
    Render al HTML de contact
    """
    imagen_de_fondo_ccs = 'contact'
    active_nav = 'contact'
    contexto = {
        'imagen_ccs': imagen_de_fondo_ccs,
        'active_nav': active_nav
    }
    return render(request, 'core/contact.html', contexto)

def portfolio(request):
    """
    Render al HTML de portfolio
    """
    
    imagen_de_fondo_ccs = 'portfolio'
    active_nav = 'portfolio'
    contexto = {
        'imagen_ccs': imagen_de_fondo_ccs,
        'active_nav': active_nav
    }
    return render(request, 'portfolio/portfolio.html', contexto)

def portfolio2(request):
    """
    Render al HTML de portfolio
    """
    
    imagen_de_fondo_ccs = 'portfolio'
    active_nav = 'portfolio'
    proyectos = Proyecto.objects.all()
    habilidades = Habilidad.objects.all()
    contexto = {
        'imagen_ccs': imagen_de_fondo_ccs,
        'active_nav': active_nav,
        'proyectos': proyectos,
        'habilidades': habilidades
    }
    return render(request, 'core/home.html', contexto)