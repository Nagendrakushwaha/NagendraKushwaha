with open('f:/NagendraKushwaha/scratch_ref/header.svg', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
# look for brackets or lines near the portrait (x around 2500 - 3500, y around 100 - 800)
for m in re.finditer(r'<path[^>]+>', text):
    p = m.group(0)
    if 'd=' in p and any(k in p for k in ['M2', 'M3', '39ff7a', 'glow']):
        print("PATH:", p[:100])

for m in re.finditer(r'<g[^>]+>', text):
    if 'id=' in m.group(0):
        print("G ID:", m.group(0))
