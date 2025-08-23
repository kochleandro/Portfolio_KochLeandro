import json
from pathlib import Path
BASE = Path(__file__).resolve().parent.parent
manifest_path = BASE / 'staticfiles' / 'staticfiles.json'
print('Manifest:', manifest_path)
manifest = json.loads(manifest_path.read_text())
keys = set(manifest.get('paths', {}).keys())
for p in [
    'core/docs/CV_2025_Leandro_Koch.pdf',
    'core/docs/CV 2025 Leandro Koch.pdf',
    'core/img/favicon.png',
    'core/iconos/NumPy_Logo.png',
    'core/iconos/NumPy_Logo.webp',
]:
    print(p, '->', p in keys)
# optionally print a sample of keys under core/iconos
iconos = [k for k in keys if k.startswith('core/iconos/')][:50]
print('\nSample iconos entries (count):', len([k for k in keys if k.startswith('core/iconos/')] ))
for k in iconos:
    print('-', k)
