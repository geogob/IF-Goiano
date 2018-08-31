#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 14:55:19 2018

@author: george
"""
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 11:14:39 2014
@author: gob
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from skimage import img_as_float
from skimage.restoration import denoise_tv_chambolle, denoise_bilateral

lena = img_as_float(np.array(Image.open('dataset/Com ferrugem/com-01.jpg')))
#lena = lena[100:300, 100:320]
#lena_rgb = lena.convert("RGB") 
#lena_gray = lena_rgb.split()[0]



noisy = lena + 0.6 * lena.std() * np.random.random(lena.shape)
noisy = np.clip(noisy, 0, 1)

fig, ax = plt.subplots(nrows=2, ncols=3, figsize=(8, 5))
fig.suptitle('George O. Barros - Noisy redution (scikit-image)')

plt.gray()

ax[0, 0].imshow(noisy)
ax[0, 0].axis('off')
ax[0, 0].set_title('noisy')

ax[0, 1].imshow(denoise_tv_chambolle(noisy, weight=0.1, multichannel=True))
ax[0, 1].axis('off')
ax[0, 1].set_title('TV')

ax[0, 2].imshow(denoise_bilateral(noisy, sigma_range=0.05, sigma_spatial=15))
ax[0, 2].axis('off')
ax[0, 2].set_title('Bilateral')

ax[1, 0].imshow(denoise_tv_chambolle(noisy, weight=0.2, multichannel=True))
ax[1, 0].axis('off')
ax[1, 0].set_title('(more) TV')

ax[1, 1].imshow(denoise_bilateral(noisy, sigma_range=0.1, sigma_spatial=15))
ax[1, 1].axis('off')
ax[1, 1].set_title('(more) Bilateral')

ax[1, 2].imshow(lena)
ax[1, 2].axis('off')
ax[1, 2].set_title('original')

fig.subplots_adjust(wspace=0.02, hspace=0.2, top=0.9, bottom=0.05, left=0, right=1)

plt.show()