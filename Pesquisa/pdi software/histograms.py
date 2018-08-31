#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 10:07:35 2018

@author: george
"""


from skimage.filters import threshold_local, threshold_otsu, threshold_mean, threshold_niblack, threshold_sauvola, threshold_minimum
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from skimage import img_as_float
#from skimage.restoration import denoise_tv_chambolle, denoise_bilateral
import matplotlib.image as mpimg
from skimage.color import rgb2hed
import pymorph as morph
from skimage.feature import daisy


img=mpimg.imread('dataset/Com ferrugem/com-02.jpg')
ihc_rgb = img
ihc_hed = rgb2hed(ihc_rgb)

#lena = img_as_float(np.array(Image.open('dataset/Com ferrugem/com-01.jpg')))
image = ihc_hed[:, :, 0] #img[:,:,0]

#thrsh2
thresh_min = threshold_mean(image)
binary_min = image > thresh_min-0.1

fig, ax = plt.subplots(2, 2, figsize=(10, 10))

ax[0, 0].imshow(image, cmap=plt.cm.gray)
ax[0, 0].set_title('Original')

ax[0, 1].hist(image.ravel(), bins=256)
ax[0, 1].set_title('Histogram')

ax[1, 0].imshow(binary_min, cmap=plt.cm.gray)
ax[1, 0].set_title('Thresholded (min)')

ax[1, 1].hist(image.ravel(), bins=256)
ax[1, 1].axvline(thresh_min, color='r')

for a in ax[:, 0]:
    a.axis('off')
plt.show()
