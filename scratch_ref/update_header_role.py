import re
import xml.etree.ElementTree as ET

with open('assets/header.svg', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Update <title>
c = re.sub(
    r'<title>.*?</title>',
    '<title>NAGENDRA KUSHWAHA - DATA SCIENCE &amp; AI ENGINEER</title>',
    c
)

# 2. Update <clipPath id="roleclip"> width animation: expand to 2000 so nothing ever clips
roleclip_old = re.search(r'<clipPath id="roleclip">.*?</clipPath>', c, re.DOTALL)
if roleclip_old:
    print("Found old roleclip:\n", roleclip_old.group(0))

new_roleclip = '''<clipPath id="roleclip"><rect x="160" y="530" width="0" height="120">
      <animate attributeName="width" from="0" to="2000" begin="2s" dur="1.2s" fill="freeze"/>
    </rect></clipPath>'''

c = re.sub(r'<clipPath id="roleclip">.*?</clipPath>', new_roleclip, c, flags=re.DOTALL)

# 3. Update the text itself:
# font-size="74" letter-spacing="14" to fit perfectly with ample breathing room
new_text = '<text class="m" x="170" y="620" font-size="74" font-weight="700" letter-spacing="14" fill="#39ff7a" filter="url(#glowsm)">DATA SCIENCE &amp; AI ENGINEER</text>'

c = re.sub(
    r'<text class="m" x="170" y="620"[^>]*>.*?</text>',
    new_text,
    c
)

# 4. Update the blinking typing cursor:
# End x = 170 + (26 * (74 * 0.6 + 14)) ~ 170 + 1518 = 1690 ~ 1700
new_cursor = '<rect class="blink" x="170" y="550" width="26" height="82" fill="#39ff7a" opacity="0"><animate attributeName="x" from="170" to="1700" begin="2s" dur="1.2s" fill="freeze"/><animate attributeName="opacity" from="0" to="1" begin="2s" dur="0.01s" fill="freeze"/></rect>'

c = re.sub(
    r'<rect class="blink" x="170" y="550"[^>]*>.*?</rect>',
    new_cursor,
    c
)

# Verify valid XML
ET.fromstring(c)

with open('assets/header.svg', 'w', encoding='utf-8') as f:
    f.write(c)

with open('scratch_ref/header.svg', 'w', encoding='utf-8') as f:
    f.write(c)

print("SUCCESS: Updated assets/header.svg with DATA SCIENCE & AI ENGINEER!")
