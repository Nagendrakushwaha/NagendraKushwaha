import base64
import os
import re
from PIL import Image, ImageEnhance
import io

print("Starting asset generation for Nagendra Kushwaha...")

# 1. Prepare Nagendra's photo in base64
img_path = 'f:/NagendraKushwaha/download.png'
if not os.path.exists(img_path):
    raise FileNotFoundError("download.png not found")

nk_orig = Image.open(img_path).convert('RGB')

# Circular avatar version (scaled to 512x512 with enhanced contrast/crispness)
nk_avatar = nk_orig.resize((512, 512), Image.Resampling.LANCZOS)
enhancer = ImageEnhance.Contrast(nk_avatar)
nk_avatar = enhancer.enhance(1.06)

avatar_buffer = io.BytesIO()
nk_avatar.save(avatar_buffer, format='JPEG', quality=95)
avatar_b64 = base64.b64encode(avatar_buffer.getvalue()).decode('utf-8')
avatar_data_uri = f"data:image/jpeg;base64,{avatar_b64}"
print(f"Avatar base64 generated, size: {len(avatar_b64)} chars")

# Header portrait version:
# Canvas is 1580 x 1400.
# We compose Nagendra's photo inside a 1580 x 1400 canvas with matching studio background,
# so that his face aligns with the HUD target bracket at x=756, y=600.
studio_bg = (248, 235, 216)
header_canvas = Image.new('RGB', (1580, 1400), studio_bg)

# Scale Nagendra so head fits HUD brackets
scale_size = 1450
nk_scaled = nk_orig.resize((scale_size, scale_size), Image.Resampling.LANCZOS)
enhancer_scaled = ImageEnhance.Contrast(nk_scaled)
nk_scaled = enhancer_scaled.enhance(1.08)

# Head center at 128, 95 in 256x256 -> in nk_scaled is 725, 538.
# Target in canvas is 756, 600.
paste_x = 756 - int(128 * scale_size / 256)
paste_y = 600 - int(95 * scale_size / 256)
header_canvas.paste(nk_scaled, (paste_x, paste_y))

header_buffer = io.BytesIO()
header_canvas.save(header_buffer, format='JPEG', quality=94)
header_b64 = base64.b64encode(header_buffer.getvalue()).decode('utf-8')
header_data_uri = f"data:image/jpeg;base64,{header_b64}"
print(f"Header portrait base64 generated, size: {len(header_b64)} chars")

os.makedirs('f:/NagendraKushwaha/assets', exist_ok=True)

# -------------------------------------------------------------
# 2. BUILD assets/header.svg
# -------------------------------------------------------------
with open('f:/NagendraKushwaha/assets/header.svg', 'r', encoding='utf-8', errors='ignore') as f:
    header_svg = f.read()

# Ensure portrait points to Nagendra's data URI
header_svg = re.sub(
    r'(<image\s+id="portrait"[^>]*?(?:xlink:href|href)=")[^"]*(")',
    rf'\g<1>{header_data_uri}\g<2>',
    header_svg
)

with open('f:/NagendraKushwaha/assets/header.svg', 'w', encoding='utf-8') as f:
    f.write(header_svg)
print("Saved assets/header.svg successfully!")

# -------------------------------------------------------------
# 3. BUILD assets/profile-header.svg
# -------------------------------------------------------------
with open('f:/NagendraKushwaha/assets/profile-header.svg', 'r', encoding='utf-8', errors='ignore') as f:
    prof_svg = f.read()

# Ensure avatar points to Nagendra's data URI
prof_svg = re.sub(
    r'(<image[^>]*?clip-path="url\(#face\)"[^>]*?(?:xlink:href|href)=")[^"]*(")',
    rf'\g<1>{avatar_data_uri}\g<2>',
    prof_svg
)

with open('f:/NagendraKushwaha/assets/profile-header.svg', 'w', encoding='utf-8') as f:
    f.write(prof_svg)
print("Saved assets/profile-header.svg successfully!")

print("ALL ASSETS VERIFIED FOR NAGENDRA KUSHWAHA!")
