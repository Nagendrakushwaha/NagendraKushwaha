import base64
import os
import re
from PIL import Image, ImageEnhance
import io

print("Configuring header portrait for Nagendra Kushwaha...")

# 1. Load download.png
nk_img = Image.open('f:/NagendraKushwaha/download.png').convert('RGB')
print("Loaded download.png, size:", nk_img.size)

# Create 1580 x 1400 canvas for header portrait
# The target HUD bracket in header.svg is:
# x in SVG = [2770, 3380], width = 610, center_x = 3075
# y in SVG = [270, 1085], height = 815, center_y = 677.5
# Since image origin is x = 2319, y = 55:
# Center of HUD in image coordinates is:
# hud_img_x = 3075 - 2319 = 756
# hud_img_y = 677.5 - 55 = 622.5

target_scale = 1500
nk_scaled = nk_img.resize((target_scale, target_scale), Image.Resampling.LANCZOS)

# Enhance contrast and sharpness so it's crisp in 4K resolution
enhancer = ImageEnhance.Contrast(nk_scaled)
nk_scaled = enhancer.enhance(1.10)
enhancer_sharp = ImageEnhance.Sharpness(nk_scaled)
nk_scaled = enhancer_sharp.enhance(1.20)

paste_x = 756 - int(128 * target_scale / 256)
paste_y = 620 - int(95 * target_scale / 256)

bg_color = (248, 235, 216)
canvas = Image.new('RGB', (1580, 1400), bg_color)
canvas.paste(nk_scaled, (paste_x, paste_y))

buf = io.BytesIO()
canvas.save(buf, format='JPEG', quality=95)
b64_data = base64.b64encode(buf.getvalue()).decode('utf-8')
data_uri = f"data:image/jpeg;base64,{b64_data}"
print("Generated Nagendra portrait data URI, length:", len(b64_data))

canvas.save('f:/NagendraKushwaha/scratch_ref/nagendra_header_canvas.jpg', quality=95)

# 2. Read assets/header.svg
with open('f:/NagendraKushwaha/assets/header.svg', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

new_image_tag = f'<image id="portrait" x="2319" y="55" width="1580" height="1400" xlink:href="{data_uri}" href="{data_uri}"/>'

content_fixed = re.sub(
    r'<image\s+id="portrait"[^>]+>',
    new_image_tag,
    content
)

with open('f:/NagendraKushwaha/assets/header.svg', 'w', encoding='utf-8') as f:
    f.write(content_fixed)

print("SUCCESS: assets/header.svg updated with Nagendra Kushwaha's image!")
