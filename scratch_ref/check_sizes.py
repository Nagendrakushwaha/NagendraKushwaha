from PIL import Image

sp = Image.open('f:/NagendraKushwaha/scratch_ref/shahid_portrait.jpg')
print("Shahid portrait dimensions:", sp.size)

nk = Image.open('f:/NagendraKushwaha/download.png')
print("Nagendra photo dimensions:", nk.size)
