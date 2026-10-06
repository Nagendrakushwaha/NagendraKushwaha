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

target_scale = 1480
nk_scaled = nk_orig.resize((target_scale, target_scale), Image.Resampling.LANCZOS)
enhancer = ImageEnhance.Contrast(nk_scaled)
nk_scaled = enhancer.enhance(1.10)
enhancer_sharp = ImageEnhance.Sharpness(nk_scaled)
nk_scaled = enhancer_sharp.enhance(1.20)

studio_bg = (248, 235, 216)
canvas = Image.new('RGB', (1580, 1400), studio_bg)
canvas.paste(nk_scaled, (16, 71))

buf = io.BytesIO()
canvas.save(buf, format='JPEG', quality=95)
portrait_b64 = base64.b64encode(buf.getvalue()).decode('utf-8')
portrait_data_uri = f"data:image/jpeg;base64,{portrait_b64}"
print(f"Portrait data URI created, length: {len(portrait_b64)}")

# 2. Read assets/header.svg
with open('f:/NagendraKushwaha/assets/header.svg', 'r', encoding='utf-8', errors='ignore') as f:
    header = f.read()

# Replace portrait with Nagendra's photo
new_portrait_tag = f'<image id="portrait" x="2319" y="55" width="1580" height="1400" xlink:href="{portrait_data_uri}" href="{portrait_data_uri}"/>'
header = re.sub(r'<image\s+id="portrait"[^>]+>', new_portrait_tag, header)

target_file = 'f:/NagendraKushwaha/assets/header.svg'
with open(target_file, 'w', encoding='utf-8') as f:
    f.write(header)

print(f"SUCCESS: Saved {target_file} ({os.path.getsize(target_file)} bytes)")
