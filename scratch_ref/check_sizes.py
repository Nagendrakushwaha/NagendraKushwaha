from PIL import Image

sp = Image.open('f:/NagendraKushwaha/scratch_ref/nagendra_header_canvas.jpg')
print("Nagendra canvas dimensions:", sp.size)

nk = Image.open('f:/NagendraKushwaha/download.png')
print("Nagendra photo dimensions:", nk.size)
