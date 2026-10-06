import re

with open('assets/header.svg', 'r', encoding='utf-8') as f:
    c = f.read()

m = re.search(r'(<clipPath id="roleclip".*?</clipPath>)', c, re.DOTALL)
if m:
    print('ROLECLIP DEF:')
    print(m.group(1))

for line in c.splitlines():
    if 'roleclip' in line or 'DATA' in line:
        print('LINE:', line[:140])
