#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 12:40:50 2023

@author: bruno.souza
"""

##### READING IMAGES IN PYTHON

#%% PACKAGES
# from PIL import Image
# import matplotlib.pyplot as plt
# from skimage import io
# import cv2 
# import numpy as np

#%% PILLOW - basic processing
# from PIL import Image

# img=Image.open('teste.png')
# print(type(img))
# img.show()
# print(img.format)

#%% PYPLOT - it's plot library
# import matplotlib.pyplot as plt
# img=plt.imread('teste.png')
# print(type(img))
# plt.imshow(img)
# plt.axis('off')0
# plt.colorbar()

#%% SKIMAGE - it's numpy array
# from skimage import io
# import matplotlib.pyplot as plt

# img=io.imread('teste.png')
# print(type(img))
# plt.imshow(img)
# plt.axis('off')


#%% OPEN CV - used for computer vision, live video
# import images as BGR - Blue/Green/Red
# import cv2 
# from matplotlib import pyplot as plt

# img=cv2.imread('teste.png')
# grey_img=cv2.imread('teste.png',0)
# color_img=cv2.imread('teste.png',1)

# How to show images: first way
# plt.imshow(img)                                      # the image colors are different because the channels are BGR
# plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))        # convert the colors channels from BGR to RGB                

# How to show images: second way
# cv2.imshow('g',color_img)
# cv2.waitKey(20000)
# cv2.destroyAllWindows()

#%% CONVERT THE IMAGE TO NUMPY ARRAY
# img1=np.asarray(img)
# print(type(img1))

#%%  How to read multiple images
# import cv2
# import glob
# from matplotlib import pyplot as plt
# import time
# from skimage import io

# path="TESTE/A/*"

# for file in glob.glob(path):
    
#     a=io.imread(file)
#     plt.imshow(a)
