import os
import re
from pathlib import Path

root = Path('.')
html_files = list(root.glob('*.html'))
missing = []

pattern = re.compile(r'(?:href|src)\s*=\s*"([^"]+)"')
for f in html_files:
    text = f.read_text(encoding='utf-8')
    for m in pattern.findall(text):
        if m.startswith('http') or m.startswith('#') or m.startswith('mailto:'):
            continue
        # normalize path
        p = (root / m).resolve()
        if not p.exists():
            missing.append((str(f), m))

if not missing:
    print('OK: Keine fehlenden lokalen Links/Dateien gefunden.')
else:
    print('Fehlende Dateien/Links:')
    for f,m in missing:
        print(f" - in {f}: {m}")
    exit(1)
