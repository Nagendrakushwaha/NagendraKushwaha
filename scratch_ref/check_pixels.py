from PIL import Image

sp = Image.open('f:/NagendraKushwaha/scratch_ref/nagendra_header_canvas.jpg')
print("Top-left pixel:", sp.getpixel((0, 0)))
print("Top-right pixel:", sp.getpixel((1579, 0)))
print("Bottom-left pixel:", sp.getpixel((0, 1399)))
print("Center pixel:", sp.getpixel((790, 700)))

nk = Image.open('f:/NagendraKushwaha/download.png')
print("NK Top-left pixel:", nk.getpixel((0, 0)))
print("NK Top-right pixel:", nk.getpixel((255, 0)))
print("NK Bottom-left pixel:", nk.getpixel((0, 255)))
print("NK Center pixel:", nk.getpixel((128, 128)))
