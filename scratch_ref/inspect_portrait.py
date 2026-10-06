import re

with open('f:/NagendraKushwaha/scratch_ref/header.svg', 'r', encoding='utf-8', errors='ignore') as f:
    header = f.read()

# Let's find where 'portrait' is used in header.svg
for line in header.splitlines():
    if 'portrait' in line or 'bgimg' in line:
        # truncate long data uris
        print(re.sub(r'data:[^"]+', 'data:...', line)[:120])

# Also let's search for masks or clipPaths or rects referring to portrait
for m in re.finditer(r'<use[^>]*>', header):
    print("USE:", m.group(0))

for m in re.finditer(r'<(mask|clipPath)\s+id="([^"]+)"', header):
    print("DEF:", m.group(1), m.group(2))
