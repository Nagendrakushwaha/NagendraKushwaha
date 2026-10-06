import numpy as np
from PIL import Image, ImageFilter, ImageOps, ImageEnhance
from scipy.ndimage import binary_fill_holes

nk = Image.open('f:/NagendraKushwaha/download.png').convert('RGB')
arr = np.array(nk, dtype=float)

# Background color reference
bg_ref = np.array([248.5, 236.0, 216.5])
diff = np.linalg.norm(arr - bg_ref, axis=2)

# Foreground mask: where diff > 25
# Let's create a smooth alpha transition between diff=15 and diff=40
alpha = np.clip((diff - 15) / 25.0, 0.0, 1.0)

# Fill holes inside the subject (his shirt is white, but distinct from cream wall)
# Check white shirt color: shirt is bright white (255, 255, 255) with collar/tie
# Any holes in the lower body should definitely be solid 1.0
h, w = alpha.shape
# The person occupies the central/bottom region
binary_fg = (alpha > 0.4)
binary_fg = binary_fill_holes(binary_fg)
alpha_filled = np.maximum(alpha, binary_fg.astype(float))

# Smooth the alpha mask slightly
alpha_img = Image.fromarray((alpha_filled * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.2))

# Upscale Nagendra and alpha to 1200x1200
nk_1200 = nk.resize((1200, 1200), Image.Resampling.LANCZOS)
alpha_1200 = alpha_img.resize((1200, 1200), Image.Resampling.LANCZOS)

# Create 1580x1400 canvas in deep emerald dark: #020a05 (RGB: 2, 10, 5)
canvas = Image.new('RGBA', (1580, 1400), (2, 10, 5, 255))

# Optional: Add a subtle cyber rim / glow behind him
glow = Image.new('RGBA', (1580, 1400), (0, 0, 0, 0))
glow_draw = Image.new('L', (1580, 1400), 0)

# Paste Nagendra so his face center is at (756, 580)
# Face center in nk_1200 is at (600, 440)
paste_x = 756 - 600
paste_y = 580 - 440

# Add alpha to nk_1200
nk_rgba = nk_1200.convert('RGBA')
nk_rgba.putalpha(alpha_1200)

canvas.paste(nk_rgba, (paste_x, paste_y), nk_rgba)

# Convert to RGB and save
final_portrait = canvas.convert('RGB')
final_portrait.save('f:/NagendraKushwaha/scratch_ref/nk_cyber_portrait.jpg', quality=95)
print("Saved nk_cyber_portrait.jpg successfully!")
