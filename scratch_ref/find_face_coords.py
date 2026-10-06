from PIL import Image

sp = Image.open('f:/NagendraKushwaha/scratch_ref/nagendra_header_canvas.jpg')
print("Nagendra canvas dimensions:", sp.size)
# x in SVG = 2319 + px_x, y in SVG = 55 + px_y
# So x=3075 in SVG corresponds to px_x = 3075 - 2319 = 756
# y=677 in SVG corresponds to px_y = 677 - 55 = 622
print("Target center in portrait coordinates: (756, 622)")

nk = Image.open('f:/NagendraKushwaha/download.png')
print("Nagendra photo size:", nk.size)
# In Nagendra's 256x256 photo, face center is around y=95, x=128
