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
# Shahid's portrait was 1580 x 1400.
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
with open('f:/NagendraKushwaha/scratch_ref/header.svg', 'r', encoding='utf-8', errors='ignore') as f:
    header_svg = f.read()

# Replace Shahid portrait with Nagendra portrait
header_svg = re.sub(
    r'(<image\s+id="portrait"[^>]*?(?:xlink:href|href)=")[^"]*(")',
    rf'\g<1>{header_data_uri}\g<2>',
    header_svg
)

# Replace title and role in header_svg
# In header_svg:
# <text ...>SHAHID AZAM</text> -> <text ...>NAGENDRA KUSHWAHA</text>
header_svg = header_svg.replace('SHAHID AZAM', 'NAGENDRA KUSHWAHA')
header_svg = header_svg.replace('Shahid Azam', 'Nagendra Kushwaha')
header_svg = header_svg.replace('DATA SCIENTIST', 'DATA SCIENTIST &amp; AI ENGINEER')

# Adjust name font size and letter-spacing for NAGENDRA KUSHWAHA so it fits nicely
# Originally: font-size="252" font-weight="800" letter-spacing="14"
header_svg = header_svg.replace('font-size="252" font-weight="800" letter-spacing="14"', 'font-size="180" font-weight="800" letter-spacing="8"')
# In nameclip: width from 0 to 2300 -> to 2600
header_svg = header_svg.replace('to="2300"', 'to="2600"')

with open('f:/NagendraKushwaha/assets/header.svg', 'w', encoding='utf-8') as f:
    f.write(header_svg)
print("Saved assets/header.svg successfully!")

# -------------------------------------------------------------
# 3. BUILD assets/ai-specialization.svg
# -------------------------------------------------------------
with open('f:/NagendraKushwaha/scratch_ref/ai-specialization.svg', 'r', encoding='utf-8', errors='ignore') as f:
    ai_svg = f.read()

with open('f:/NagendraKushwaha/assets/ai-specialization.svg', 'w', encoding='utf-8') as f:
    f.write(ai_svg)
print("Saved assets/ai-specialization.svg successfully!")

# -------------------------------------------------------------
# 4. BUILD assets/profile-header.svg
# -------------------------------------------------------------
with open('f:/NagendraKushwaha/scratch_ref/profile-header.svg', 'r', encoding='utf-8', errors='ignore') as f:
    prof_svg = f.read()

# Replace Shahid portrait with Nagendra avatar
prof_svg = re.sub(
    r'(<image[^>]*?clip-path="url\(#face\)"[^>]*?(?:xlink:href|href)=")[^"]*(")',
    rf'\g<1>{avatar_data_uri}\g<2>',
    prof_svg
)

# Replace texts
prof_svg = prof_svg.replace('Shahid Azam', 'Nagendra Kushwaha')
prof_svg = prof_svg.replace('SHAHID AZAM', 'NAGENDRA KUSHWAHA')
prof_svg = prof_svg.replace('MS Computer Science, specialization in Artificial Intelligence', 'B.Tech CSE, Specialization in AI &amp; Data Science')
prof_svg = prof_svg.replace('Institute of Management Sciences, Peshawar', 'Sam Global University, Bhopal')
prof_svg = prof_svg.replace('40+', '30+')
prof_svg = prof_svg.replace('Projects on Kaggle', 'Projects on GitHub')
prof_svg = prof_svg.replace('20K+', 'Open')
prof_svg = prof_svg.replace('LinkedIn followers', 'To AI/ML Roles')
prof_svg = prof_svg.replace('Jupyter Notebook', 'FastAPI / PyTorch')

# Also adjust title / desc
prof_svg = re.sub(r'<title id="t">.*?</title>', '<title id="t">Nagendra Kushwaha, Data Scientist</title>', prof_svg)
prof_svg = re.sub(r'<desc id="d">.*?</desc>', '<desc id="d">Profile banner of Nagendra Kushwaha, Data Scientist and AI/ML Engineer.</desc>', prof_svg)

with open('f:/NagendraKushwaha/assets/profile-header.svg', 'w', encoding='utf-8') as f:
    f.write(prof_svg)
print("Saved assets/profile-header.svg successfully!")

# -------------------------------------------------------------
# 5. BUILD assets/github-stats.svg
# -------------------------------------------------------------
with open('f:/NagendraKushwaha/scratch_ref/github-stats.svg', 'r', encoding='utf-8', errors='ignore') as f:
    stats_svg = f.read()

stats_svg = stats_svg.replace('Shahid Azam, Data Scientist', 'Nagendra Kushwaha, Data Scientist &amp; AI Engineer')
stats_svg = stats_svg.replace('Shahid Azam', 'Nagendra Kushwaha')

with open('f:/NagendraKushwaha/assets/github-stats.svg', 'w', encoding='utf-8') as f:
    f.write(stats_svg)
print("Saved assets/github-stats.svg successfully!")

# -------------------------------------------------------------
# 6. BUILD assets/spent-my-time.svg
# -------------------------------------------------------------
with open('f:/NagendraKushwaha/scratch_ref/spent-my-time.svg', 'r', encoding='utf-8', errors='ignore') as f:
    spent_svg = f.read()

spent_svg = spent_svg.replace('Shahid Azam', 'Nagendra Kushwaha')

with open('f:/NagendraKushwaha/assets/spent-my-time.svg', 'w', encoding='utf-8') as f:
    f.write(spent_svg)
print("Saved assets/spent-my-time.svg successfully!")

print("ALL ASSETS SUCCESSFULLY GENERATED!")
