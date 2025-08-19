"""
Configuración de ASGI para el proyecto porfolio_web.

Expone la llamada ASGI como una variable a nivel de módulo denominada ``application``

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'porfolio_web.settings')

application = get_asgi_application()
