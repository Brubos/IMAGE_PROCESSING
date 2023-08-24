#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 08:34:59 2023

@author: bruno.souza
"""

#%% PACKAGES
from PIL import Image

#%% Read a image
# img = Image.open('teste.png')
# print(img.mode)                     # show the mode of image 
# print(img.size)                     # show the size of the image


#%% Resize x Thumbnail  - resize don't keep the aspect ratio, while thumbnail do 

# small_img = img.resize((300,300))   # change the image dimensions (squishe)
# small_img.save('small_image.jpg')   # save the image

# img.thumbnail((300,300))            # resize the image but keep the proportion
# img.save('image_test.png')

#%% Crop a image

# cropped_img = img.crop((30,50,300,250))     
# cropped_img.save('cropped.png')

#%% Copy and paste images

# img1 = Image.open('teste.png') 
# img2 = Image.open('foco002.png')

# img2 = img2.resize((200,200))

# img1_copy = img1.copy()
# img1_copy.paste(img2,(0,50))
# mod = img1_copy.save('modified_image.png')

#%% Image rotation

# img = Image.open('teste.png') 
# img45 = img.rotate(45, expand= False)

#%% Image tranpose

img = Image.open('teste.png') 
img_flipLR = img.transpose(Image.FLIP_LEFT_RIGHT)
img_flipTB = img.transpose(Image.FLIP_TOP_BOTTOM)

#%%

grey_img = img.convert("L")
