import os
import sys
from pathlib import Path
# Ensure project root is on sys.path so `porfolio_web` is importable when running from scripts/
proj_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(proj_root))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'porfolio_web.settings')
# Force DEBUG False for the settings that use decouple
os.environ['DEBUG'] = 'False'
# Allow async unsafe when running tests this way
os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'

import django
django.setup()
from django.test import Client
c = Client()
resp = c.get('/', SERVER_NAME='localhost', HTTP_HOST='localhost')
print('STATUS', resp.status_code)
# Print start of content or exception detail
try:
    print(resp.content.decode('utf-8')[:800])
except Exception:
    print(repr(resp.content))
