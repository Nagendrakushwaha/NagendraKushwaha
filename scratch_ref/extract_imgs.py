import re
import base64
from io import BytesIO
from PIL import Image

with open('f:/NagendraKushwaha/scratch_ref/header.svg', 'r', encoding='utf-8', errors='ignore') as f:
    header = f.read()

# find portrait image
m = re.search(r'id="portrait"[^>]*?(xlink:href|href)="data:image/([^;]+);base64,([^"]+)"', header)
if m:
    ext = m.group(2)
    b64 = m.group(3)
    img_data = base64.b64decode(b64)
    img = Image.open(BytesIO(img_data))
    print(f"Shahid Portrait: format={img.format}, size={img.size}, mode={img.mode}")
    img.save('f:/NagendraKushwaha/scratch_ref/shahid_portrait.jpg')

m2 = re.search(r'id="bgimg"[^>]*?(xlink:href|href)="data:image/([^;]+);base64,([^"]+)"', header)
if m2:
    ext = m2.group(2)
    b64 = m2.group(3)
    img_data = base64.b64decode(b64)
    img = Image.open(BytesIO(img_data))
    print(f"BG img: format={img.format}, size={img.size}, mode={img.mode}")
    img.save('f:/NagendraKushwaha/scratch_ref/shahid_bg.jpg')
