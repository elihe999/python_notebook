#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from PIL import Image
from PIL import ImageEnhance

img = Image.open('./Switch_Line.png')
#print(img.size)
w, h = img.size
print(w,h)
#print(img.mode)

enh = ImageEnhance.Contrast(img)
enh.enhance(1.3).show("30%")

#box = (1, 100, 400, 400)
#region = img.crop(box)
#region.show()
#new_img = img.convert('L')
#print(new_img.mode)
#new_img.getpixel((0,0))
#new_img.show()

