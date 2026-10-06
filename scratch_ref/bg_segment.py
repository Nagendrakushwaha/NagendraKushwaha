import numpy as np
from PIL import Image, ImageFilter

nk = Image.open('f:/NagendraKushwaha/download.png').convert('RGB')
arr = np.array(nk)

# Sample background color in the top corners
top_left = arr[:30, :30].mean(axis=(0,1))
top_right = arr[:30, -30:].mean(axis=(0,1))
print("Top left bg color:", top_left)
print("Top right bg color:", top_right)

# Test color distance from background
bg_ref = (top_left + top_right) / 2
diff = np.linalg.norm(arr.astype(float) - bg_ref, axis=2)
print("Min diff:", diff.min(), "Max diff:", diff.max(), "Median:", np.median(diff))
