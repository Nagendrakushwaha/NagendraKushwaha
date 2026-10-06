import numpy as np
from PIL import Image, ImageFilter, ImageEnhance

# Load Nagendra's photo
nk = Image.open('f:/NagendraKushwaha/download.png').convert('RGB')

# Upscale to high resolution using Lanczos
nk_high = nk.resize((1000, 1000), Image.Resampling.LANCZOS)

# Create 1580x1400 canvas filled with the ambient dark emerald color (#03150a -> RGB 3, 21, 10)
bg_color = (3, 21, 10)
canvas = Image.new('RGB', (1580, 1400), bg_color)

# We want Nagendra's face center (which in nk_high is at approx (500, 380))
# to align with target (756, 622).
# Scale factor:
# If face width in nk_high is ~400px, in 1580x1400 canvas that fits comfortably within the 610px HUD bracket!
# Scale nk_high so head height and shoulders fill nicely
scale = 1.35
w_scaled = int(1000 * scale)
h_scaled = int(1000 * scale)
nk_scaled = nk.resize((w_scaled, h_scaled), Image.Resampling.LANCZOS)

# Face center in nk_scaled is at (int(500 * scale), int(380 * scale)) = (675, 513)
# To place face center at (756, 580):
paste_x = 756 - int(500 * scale)
paste_y = 580 - int(380 * scale)
print(f"Paste position: ({paste_x}, {paste_y}), size: ({w_scaled}, {h_scaled})")

# Let's create an alpha feather mask for nk_scaled so its off-white studio background
# blends smoothly into the dark emerald background, while keeping the subject clear
# Or let's create a soft vignette mask for the photo
mask = Image.new('L', (w_scaled, h_scaled), 255)
mask_np = np.ones((h_scaled, w_scaled), dtype=np.float32)

# Feather the edges
feather_w = int(w_scaled * 0.25)
feather_h = int(h_scaled * 0.25)

for x in range(feather_w):
    factor = np.sin((x / feather_w) * (np.pi / 2))
    mask_np[:, x] *= factor
    mask_np[:, w_scaled - 1 - x] *= factor

for y in range(feather_h):
    factor = np.sin((y / feather_h) * (np.pi / 2))
    mask_np[y, :] *= factor
    mask_np[h_scaled - 1 - y, :] *= factor

mask_img = Image.fromarray((mask_np * 255).astype(np.uint8))

# Let's paste with mask
canvas.paste(nk_scaled, (paste_x, paste_y), mask_img)

# Slight color grade: enhance contrast and slight emerald tone to fit the cyber aesthetic
enhancer = ImageEnhance.Contrast(canvas)
canvas = enhancer.enhance(1.1)

canvas.save('f:/NagendraKushwaha/scratch_ref/nk_portrait_test.jpg', quality=92)
print("Saved nk_portrait_test.jpg successfully!")
