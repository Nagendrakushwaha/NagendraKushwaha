import numpy as np
from PIL import Image, ImageEnhance, ImageFilter

# Load Nagendra's original photo
nk = Image.open('f:/NagendraKushwaha/download.png').convert('RGB')

# The studio wall background color from top corners
bg_color = (248, 235, 216)

# Create 1580x1400 canvas filled with studio wall color
canvas = Image.new('RGB', (1580, 1400), bg_color)

# We want Nagendra's head to be centered around (756, 600)
# In nk (256x256), head center is at (128, 95).
# If we scale nk to width 1400, height 1400:
# head center will be at (700, 520).
scale_size = 1450
nk_scaled = nk.resize((scale_size, scale_size), Image.Resampling.LANCZOS)

# Position so head center is at (756, 600):
pos_x = 756 - int(128 * scale_size / 256)
pos_y = 600 - int(95 * scale_size / 256)
print(f"Paste position: ({pos_x}, {pos_y})")

# Soft blend of the photo edges into the studio canvas
mask = Image.new('L', (scale_size, scale_size), 255)
# paste onto canvas
canvas.paste(nk_scaled, (pos_x, pos_y))

# Slight clarity and contrast enhancement so suit and face are crisp
enhancer = ImageEnhance.Contrast(canvas)
canvas = enhancer.enhance(1.08)

# Save high-res JPEG
canvas.save('f:/NagendraKushwaha/scratch_ref/nagendra_header_portrait.jpg', quality=95)
print("Saved nagendra_header_portrait.jpg successfully!")
