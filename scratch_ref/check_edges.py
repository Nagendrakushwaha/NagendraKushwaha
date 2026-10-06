from PIL import Image

sp = Image.open('f:/NagendraKushwaha/scratch_ref/shahid_portrait.jpg')
w, h = sp.size
print("Width:", w, "Height:", h)
# Sample along left edge
left_pixels = [sp.getpixel((0, y)) for y in range(0, h, 200)]
print("Left edge pixels:", left_pixels)
right_pixels = [sp.getpixel((w-1, y)) for y in range(0, h, 200)]
print("Right edge pixels:", right_pixels)
top_pixels = [sp.getpixel((x, 0)) for x in range(0, w, 200)]
print("Top edge pixels:", top_pixels)
bottom_pixels = [sp.getpixel((x, h-1)) for x in range(0, w, 200)]
print("Bottom edge pixels:", bottom_pixels)
