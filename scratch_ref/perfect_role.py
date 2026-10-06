import re
import xml.etree.ElementTree as ET

# 1. Update assets/header.svg
with open('assets/header.svg', 'r', encoding='utf-8') as f:
    c = f.read()

# Update aria-label
c = c.replace('DATA SCIENTIST &amp; AI ENGINEER', 'DATA SCIENCE &amp; AI ENGINEER')
c = c.replace('DATA SCIENTIST & AI ENGINEER', 'DATA SCIENCE & AI ENGINEER')

# Update clipPath to width="2200"
c = re.sub(
    r'<clipPath id="roleclip"><rect x="160" y="530" width="0" height="120">\s*<animate attributeName="width" from="0" to="[^"]+" begin="2s" dur="1.2s" fill="freeze"/>\s*</rect></clipPath>',
    '<clipPath id="roleclip"><rect x="160" y="530" width="0" height="120">\n      <animate attributeName="width" from="0" to="2200" begin="2s" dur="1.2s" fill="freeze"/>\n    </rect></clipPath>',
    c
)

# Text tag
c = re.sub(
    r'<text class="m" x="170" y="620"[^>]*>.*?</text>',
    '<text class="m" x="170" y="620" font-size="74" font-weight="700" letter-spacing="14" fill="#39ff7a" filter="url(#glowsm)">DATA SCIENCE &amp; AI ENGINEER</text>',
    c
)

# Cursor animation: stops at 1720px right after the last letter 'R'
c = re.sub(
    r'<rect class="blink" x="170" y="550"[^>]*>.*?</rect>',
    '<rect class="blink" x="170" y="550" width="26" height="82" fill="#39ff7a" opacity="0"><animate attributeName="x" from="170" to="1720" begin="2s" dur="1.2s" fill="freeze"/><animate attributeName="opacity" from="0" to="1" begin="2s" dur="0.01s" fill="freeze"/></rect>',
    c
)

# Validate XML
ET.fromstring(c)

with open('assets/header.svg', 'w', encoding='utf-8') as f:
    f.write(c)

with open('scratch_ref/header.svg', 'w', encoding='utf-8') as f:
    f.write(c)

print("assets/header.svg successfully updated and validated!")

# 2. Update Readme.md
with open('Readme.md', 'r', encoding='utf-8') as f:
    r = f.read()

r = r.replace('Nagendra Kushwaha — Data Scientist & AI/ML Engineer', 'Nagendra Kushwaha — Data Science & AI Engineer')
r = r.replace('**Data Scientist & AI/ML Engineer**', '**Data Science & AI Engineer**')

with open('Readme.md', 'w', encoding='utf-8') as f:
    f.write(r)

print("Readme.md updated consistently!")
