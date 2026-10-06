import base64
import os
import re
from PIL import Image, ImageEnhance
import io

print("Generating final perfected header.svg for Nagendra Kushwaha...")

# 1. Load download.png (Nagendra's photo)
nk_path = 'f:/NagendraKushwaha/download.png'
nk_orig = Image.open(nk_path).convert('RGB')
print(f"Loaded {nk_path}, size: {nk_orig.size}")

# Target HUD bracket in header.svg:
# x in SVG: [2770, 3380], width = 610, center_x = 3075
# y in SVG: [270, 1085], height = 815, center_y = 677.5
# Image placed at x = 2319, y = 55, size = 1580 x 1400.
# So in 1580x1400 coordinates:
# HUD center is (3075 - 2319, 677.5 - 55) = (756, 622.5)

# In Nagendra's 256x256 image, head center is at (128, 95).
# If we scale download.png to 1480x1480:
# head center in scaled image is (740, 549).
# To place head at (756, 620):
# paste_x = 756 - 740 = 16
# paste_y = 620 - 549 = 71

target_scale = 1480
nk_scaled = nk_orig.resize((target_scale, target_scale), Image.Resampling.LANCZOS)
enhancer = ImageEnhance.Contrast(nk_scaled)
nk_scaled = enhancer.enhance(1.10)
enhancer_sharp = ImageEnhance.Sharpness(nk_scaled)
nk_scaled = enhancer_sharp.enhance(1.20)

# Studio background color from download.png:
studio_bg = (248, 235, 216)
canvas = Image.new('RGB', (1580, 1400), studio_bg)
canvas.paste(nk_scaled, (16, 71))

# Convert to high-quality JPEG base64 data URI
buf = io.BytesIO()
canvas.save(buf, format='JPEG', quality=95)
portrait_b64 = base64.b64encode(buf.getvalue()).decode('utf-8')
portrait_data_uri = f"data:image/jpeg;base64,{portrait_b64}"
print(f"Portrait data URI created, length: {len(portrait_b64)}")

# 2. Read scratch_ref/header.svg (the clean template)
with open('f:/NagendraKushwaha/scratch_ref/header.svg', 'r', encoding='utf-8', errors='ignore') as f:
    header = f.read()

# REMOVE <image id="bgimg" .../> COMPLETELY!
# In the original, <use href="#bgimg" xlink:href="#bgimg"/> was placed after <rect fill="#020a05"/>.
# Let's replace <image id="bgimg"...> in <defs> with an SVG radial gradient:
# <radialGradient id="cyberBgGlow" cx="70%" cy="45%" r="60%">
#   <stop offset="0%" stop-color="#0b3f20" stop-opacity="0.6"/>
#   <stop offset="60%" stop-color="#03150a" stop-opacity="0.95"/>
#   <stop offset="100%" stop-color="#020a05" stop-opacity="1"/>
# </radialGradient>
# And replace <use href="#bgimg".../> with <rect width="3840" height="1280" fill="url(#cyberBgGlow)"/>

cyber_gradient_def = '''    <radialGradient id="cyberBgGlow" cx="70%" cy="45%" r="65%">
      <stop offset="0%" stop-color="#0b3f20" stop-opacity="0.7"/>
      <stop offset="50%" stop-color="#03160b" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#020a05" stop-opacity="1"/>
    </radialGradient>'''

header = re.sub(r'<image\s+id="bgimg"[^>]+>', cyber_gradient_def, header)

# In the body, replace <use href="#bgimg" .../>
header = re.sub(r'<use\s+href="#bgimg"[^>]+/>', '<rect width="3840" height="1280" fill="url(#cyberBgGlow)"/>', header)

# Now replace <image id="portrait" ...> with Nagendra's image
# Both xlink:href and href must point to portrait_data_uri
new_portrait_tag = f'<image id="portrait" x="2319" y="55" width="1580" height="1400" xlink:href="{portrait_data_uri}" href="{portrait_data_uri}"/>'
header = re.sub(r'<image\s+id="portrait"[^>]+>', new_portrait_tag, header)

# Update texts
header = header.replace('SHAHID AZAM', 'NAGENDRA KUSHWAHA')
header = header.replace('Shahid Azam', 'Nagendra Kushwaha')
header = header.replace('DATA SCIENTIST', 'DATA SCIENTIST &amp; AI ENGINEER')

# Adjust name text size & animation width in header
header = header.replace('font-size="252" font-weight="800" letter-spacing="14"', 'font-size="180" font-weight="800" letter-spacing="8"')
header = header.replace('to="2300"', 'to="2600"')

# Verify NO old shahid signatures remain
old_sig = 'wARCAFAA8ADASIAAhEBAxEB'
if old_sig in header:
    print("WARNING: Old signature still found!")
else:
    print("VERIFIED: 100% of old image signatures completely removed!")

# Save to assets/header.svg
target_file = 'f:/NagendraKushwaha/assets/header.svg'
with open(target_file, 'w', encoding='utf-8') as f:
    f.write(header)

print(f"SUCCESS: Saved {target_file} ({os.path.getsize(target_file)} bytes)")
