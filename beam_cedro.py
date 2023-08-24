#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 17:17:03 2023

@author: sergio.lordano
"""

#%% Packages
import numpy as np
from optlnls.plot import plot_beam, plot_xy_list
import cv2
from matplotlib import image
from matplotlib import pyplot as plt
from PIL import Image
import sys
import glob


#%% Definition function

def read_beam_image(fname, px2mm=4.8e-3, window=-1, channel='RGB', center=1, background=-1, bg_pars=[0,60,0.95]):

    ### Read Image 
    
    img = cv2.imread(fname, 1)  # 1 (color image - BGR), 0 (gryscale), -1 (BGR,alfa)

    shape = img.shape

    ny, nx = shape[:2]

    ### ROI - Region of Interest
    if(window > 0):
        if(len(shape) > 2):
            img0 = np.average(img, axis=2)
                
        x = np.linspace(1, nx, nx, dtype=float)
        y = np.linspace(1, ny, ny, dtype=float)
        
        ### Remove background
        background0 = np.max(img0[bg_pars[0]:bg_pars[1],bg_pars[0]:bg_pars[1]]) * bg_pars[2]
        img0[img0 <= background0] = 0
        
        ### Find peak positions
        Ix0 = np.sum(img0, axis=0) # sum of intensities along the vertical axis (summing columns)
        Iy0 = np.sum(img0, axis=1) # sum of intensities along the horizontal axis (summing rows) 
        
        # Find the indices of Ix0 and Iy0 are maximum
        x0 = x[Ix0.argmax()] 
        y0 = x[Iy0.argmax()]
    
        # Calculates the coordinates (ro1,ro2,ro3,roi4) of the rectangular region of interest
        roi1 = int(y0-window/2) if(int(y0-window/2) >= 0) else 0
        roi2 = int(y0+window/2) if(int(y0+window/2) <= ny) else ny
        roi3 = int(x0-window/2) if(int(x0-window/2) >= 0) else 0
        roi4 = int(x0+window/2) if(int(x0+window/2) <= nx) else nx     
        # print(roi1, roi2, roi3, roi4)
        
    else:
        roi1 = 0
        roi2 = ny
        roi3 = 0
        roi4 = nx 
    
    ### Choose channel
    if(len(shape) > 2):
        r = img[roi1:roi2,roi3:roi4,0]
        g = img[roi1:roi2,roi3:roi4,1]
        b = img[roi1:roi2,roi3:roi4,2]
        
        if(channel == 'R'):
            channel = r
        elif(channel == 'G'):
            channel = g
        elif(channel == 'B'):
            channel = b
        else:
            channel = r+g+b
    else:
        channel = img[roi1:roi2,roi3:roi4]
        
    ### Remove background
    if(background < 0):
        background = np.max(channel[bg_pars[0]:bg_pars[1],bg_pars[0]:bg_pars[1]]) * bg_pars[2]
        # background = np.median(channel[0:60,0:60])          
    
    max_count = np.max(channel)
    SNR = max_count / background
    
    ny, nx = channel.shape
    x = np.linspace(1, nx, nx, dtype=float)   
    y = np.linspace(1, ny, ny, dtype=float)
    
    if(center):
        y = y - np.mean(y)
        x = x - np.mean(x)
    
    # channel = channel - background
    channel[channel <= background] = 0.0
    
    ### Create Matrix in OPT format
    mtx = np.zeros((ny+1,nx+1))
    mtx[1:,0] = y * px2mm
    mtx[0,1:] = x * px2mm
    mtx[1:,1:] = channel
    
    outdict = {'mtx':mtx,
               'SNR':SNR,
               'Max Count':max_count,
               'background':background}
    
    return outdict


#%% Plot image

# Parameters
fname = 'foco002.png'
px2mm = 4.8e-3
window = 1280  #100

channel = 'B'
# channel = 'G'
# channel = 'R'

background = -1
bg_pars = [0, 20, 1.0]
center = 1

# Aplly the function
d = read_beam_image(fname, px2mm, window, channel, center, background, bg_pars)
plt.imshow( d['mtx'])

bg = d['background']
mtx = d['mtx']
imgMTX = mtx[1:,1:]

fitType=3
savgol = [11, 3]
cmap = 'Blues' # 'viridis'


od = plot_beam(mtx, cut=0, textB=5, textC=10, textD=7, cmap=cmap, show_colorbar=0,
                plot_title='Cedro / SSA              26-07-2023', textA=1,
                fitType=fitType, isdensity=0, zlabel='counts', units=2,
                outfilename=fname[:-4]+'_b_int_FOCUS.jpg')


# sys.exit()
 



















