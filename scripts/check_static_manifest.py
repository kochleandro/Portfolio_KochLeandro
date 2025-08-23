import re
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
manifest_path = BASE / 'staticfiles' / 'staticfiles.json'
if not manifest_path.exists():
    print('No manifest found at', manifest_path)
    raise SystemExit(1)

manifest = json.loads(manifest_path.read_text())
manifest_keys = set(manifest.get('paths', {}).keys())

# Scan templates
pattern = re.compile(r"\{%%\s*static\s*['\"]([^'\"]+)['\"]\s*%%\}")
missing = {}
for tpl in (BASE / 'templates').rglob('*.html'):
    content = tpl.read_text(encoding='utf-8')
    for m in pattern.finditer(content):
        path = m.group(1)
        if path not in manifest_keys:
            missing.setdefault(path, []).append(str(tpl))

if not missing:
    print('All template static references are present in the manifest.')
else:
    print('Missing manifest entries for the following static paths:')
    for p, files in missing.items():
        print('-', p)
        for f in files[:5]:
            print('   referenced in', f)
    print('\nTotal missing:', len(missing))
