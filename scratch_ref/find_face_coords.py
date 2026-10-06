from PIL import Image

sp = Image.open('f:/NagendraKushwaha/scratch_ref/shahid_portrait.jpg')
print("Shahid portrait dimensions:", sp.size)
# x in SVG = 2319 + px_x, y in SVG = 55 + px_y
# So x=3075 in SVG corresponds to px_x = 3075 - 2319 = 756
# y=677 in SVG corresponds to px_y = 677 - 55 = 622
print("Target center in portrait coordinates: (756, 622)")

# Now let's examine download.png (Nagendra's photo)
nk = Image.open('f:/NagendraKushwaha/download.png')
print("Nagendra photo size:", nk.size)
# In Nagendra's 256x256 photo, where is his face center?
# His eyes/nose are around y=80-110, x=128
