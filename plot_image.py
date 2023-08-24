#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 09:52:01 2023

@author: sergio.lordano
"""
########### IMAGE PROCESSING  ###########
# this script obtain:
#  - plot the beam from an image
#  - remove the background  

#%% packages
import numpy as np
from optlnls.plot import plot_beam, plot_xy_list
import cv2
from matplotlib import pyplot as plt

#%% import and plot image
fname = 'foco002.png'
img = cv2.imread(fname)


# definitions and parameters
px2mm = 4.8e-3                        # datasheet camera (pixel to mm)
img = img[:,:,2]                      # choosing the first channel (BGR-Blue/Green/Red)
ny, nx = img.shape[0],img.shape[1]    # getting the dimensions of the image


# plt.imshow(img)                                 # show the image
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))   # convert the colors channels from BGR to RGB


# create arrays
x = np.linspace(1, nx, nx)
y = np.linspace(1, ny, ny)

# # create a matrix to insert an image
mtx1 = np.zeros((ny+1,nx+1))             # create a matrix with (ny+1) rows and (nx+1) columns
mtx1[0,1:]  = x * px2mm                  # fills the entire 1st line except the first element
mtx1[1:,0]  = y * px2mm                  # fills the entire first column except the first element 
mtx1[1:,1:] = img                        # insert an image from the 2nd row and column


# plot the matrix
plot_beam(mtx1, cut=2, fitType=3, textA=1,textB=5,textC=10, plot_title='CEDRO')


#%% defining a function to remove background
def remove_background_by_window(img, idx1=0, idx2=30, factor=1):
    
    '''
    Parameters
    ----------
    img : 2D array
        origin image 
        
    idx1,idx2 : int
        windows values
        
    factor : float
        atenuation factor
        
    Returns
    -------
    img: 2D numpy array
        image without background
        
     '''
        
    background = np.max(img[idx1:idx2, idx1:idx2]) * factor
    img[img <= background] = 0

    return img


#%% try to remove the background
img2 = remove_background_by_window(img, 0, 60, 1.5)
plt.figure()
plt.imshow(img2)


mtx2 = np.zeros((ny+1,nx+1))
mtx2[0,1:] = x * px2mm
mtx2[1:,0] = y * px2mm
mtx2[1:,1:] = img2

plot_beam(mtx2, cut=2, fitType=3, textA=1,textB=5,textC=10,plot_title='CEDRO')




















