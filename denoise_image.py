#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 14:25:12 2023

@author: sergio.lordano
"""
#%% Packages
import numpy as np
from matplotlib import pyplot as plt
import cv2
from copy import deepcopy
import scipy.fft as fft


#%% Defining functions
def remove_background_by_window(img, idx1=0, idx2=30, factor=1):
    
    background = np.max(img[idx1:idx2, idx1:idx2]) * factor
    img[img <= background] = 0

    return img

def remove_background_by_histogram():
    pass

def remove_background_by_FFT(img):
    pass

#%%

# Loading the image
fname = 'teste.png'
img = cv2.imread(fname)

# Convert to grayscale and find the maximum value
img = img[:,:,2]
img_max = img.max()

# Calculate the histogram
histo = np.histogram(img.flatten(), bins=1000)

# Remove the background by window
img1 = remove_background_by_window(deepcopy(img))

# Apply the denoising filter
img3 = cv2.fastNlMeansDenoising(deepcopy(img), 1500, 6, 7, 21)

# Fourier Transform and Shifting
img_FFT = np.fft.fft2(img)
img_FFT = np.fft.fftshift(img_FFT)

# Get image dimensions
ny, nx = img.shape

# Create coordinate grids
x = np.linspace(1, nx, nx) - nx/2
y = np.linspace(1, ny, ny) - ny/2
xx, yy = np.meshgrid(x,y)

# Apply a filter in the frequency domain
radius = 20
img_FFT_filter = deepcopy(img_FFT)
img_FFT_filter[xx**2 + yy**2 > radius**2] = 0
# img_FFT_filter[xx**2 > radius**2] = 0
# img_FFT_filter[yy**2 > radius**2] = 0

# Inverse Fourier Transform
img_filtered = deepcopy(img_FFT_filter)
img_filtered = fft.ifftshift(img_filtered)
img_filtered = np.abs(fft.ifft2(img_filtered))


#%% PLOTTING

# View the original image
plt.figure()
plt.imshow(img, cmap='Greys')
plt.title('Original Image')
plt.axis('off')

# View the image after background removal
plt.figure()
plt.imshow(img1, cmap='Greys')
plt.title('Image after Background Removal')
plt.axis('off')

# View the image after denoising filter
plt.figure()
plt.imshow(img3, cmap='Greys')
plt.title('Image after Denoising Filter')
plt.axis('off')

# View the histogram in logarithmic scale
plt.figure()
plt.bar(x=histo[1][1:], height=histo[0], width=0.5)
plt.yscale('log')
plt.title('Histogram (Logarithmic Scale)')
plt.xlabel('Intensity Value')
plt.ylabel('Frequency (log)')
plt.tight_layout()

# Plot the log magnitude of the Fourier Transform of the original image
plt.figure()
plt.imshow(np.log(np.abs(img_FFT)), cmap='Greys')
plt.title('Log Magnitude of Fourier Transform')

# Plot the log magnitude of the filtered Fourier Transform
plt.figure()
plt.imshow(np.log(np.abs(img_FFT_filter)), origin='lower', cmap='Greys')
plt.title('Filtered Fourier Transform')

# Plot the filtered image obtained through the inverse Fourier Transform
plt.figure()
plt.imshow(img_filtered,  cmap='Greys')
plt.title('Filtered Image (Inverse Fourier Transform)')

# Plot the magnitude of the Fourier Transform of the original image
plt.figure()
plt.imshow(np.abs(img_FFT),  cmap='Greys')
plt.title('Magnitude of Fourier Transform')

# Plot the filtered image obtained through the inverse Fourier Transform using the Viridis colormap
plt.figure()
plt.imshow(img_filtered,cmap='viridis')
plt.title('Filtered Image (Viridis colormap)')

# Plot the log magnitude of the Fourier Transform of the original image using the Viridis colormap
plt.figure()
plt.imshow(np.log(np.abs(img_FFT)), cmap='viridis')
plt.title('Log Magnitude of Fourier Transform (Viridis colormap)')

# Display all the plots
plt.show()






























