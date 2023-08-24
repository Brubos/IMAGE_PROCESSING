#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 09:02:36 2023

@author: bruno.souza
"""

#%% PACKAGES
from skimage import io
from skimage import img_as_float
import numpy as np
from matplotlib import pyplot as plt
#%% dtypes
# unit8    : 0  to (2**8  - 1)   or (0 to 255)
# unit16   : 0  to (2**16 - 1)   or (0 to 65535)
# unit 32  : 0  to (2**32 - 1)   or (0 to 4294967295)
# float    : (-1 to 1) or (0 to 1)
# int8     : -128 to 127
# int16    : -32768 to 32767
# int32    : -2**31 to (2**31 - 1)

#%% Functions that convert images to desired dtype and properly rescale their value

# img_as_float - convert to 64-bit floating point;
# img_as_ubyte - convert to 8-bit unit;
# img_as_uint  - convert to 16-bit unit;
# img_as_int   - convert to 16-bit int;

#%% Read a image (0,255)
# image4=io.imread("foco004.png")
# image2=io.imread("foco002.png")
# image14=io.imread('foco014.png')

# # Adding the three images
# new=image2+image4+image14
# plt.imshow(new)
# plt.axis('off')

#%% Read a image (0,1)
# image=io.imread("foco002.png")
# image_float=img_as_float(image)
# print(image_float.min(),image_float.max())
# plt.imshow(image)
# plt.axis('off')

#%% Plot the original image
# plt.imshow(image_float)

#%% Create a random image [n,m,s];
# n rows, m  columns, s are the channels where s=1 (viridis colormap), s=3 (RGB), s=4 (RGBA)
# rd_img=np.random.random([4,4,4])
# plt.imshow(rd_img)

#%% Create a random image [n,m,s];
# n lines, m  columns, s are the channels where s=1 (viridis colormap), s=3 (RGB), s=4 (RGBA)
# rd_img=np.random.random([3,3,3])
# plt.imshow(rd_img)

#%% Create a box with RBG colors in the image

# image=io.imread('teste.png')
# plt.imshow(image)
# plt.axis('off')
# image[0:400,0:384,:] = [255,255,255]
# plt.imshow(image)
