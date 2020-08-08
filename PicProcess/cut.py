import os
from PIL import Image

img = Image.open('./Switch_Line.png')
#print(img.size)
w, h = img.size
print(w,h)
print(img.mode)
