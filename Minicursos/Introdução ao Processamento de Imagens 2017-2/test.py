# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 06:44:20 2017

@author: George
"""
#num = 7
#num2 = 10
#
#print 'O resultado da soma é', num+num2
#print 'O resultado da subtração é', num-num2
#print 'O resultado da multiplicação é', num*num2
#print 'O resultado da divisão', num/num2
#
#lista = [78,12,11,87,7]
#print lista

import numpy as np
#a = np.arange(30)
#b = np.array([[1,2,3,4,5],
#              [10,20,30,40,50],
#              [5,5,5,5,5],
#              [5,5,5,5,5]])
#b = b.transpose

from PIL import Image
imRGB = np.array(Image.open('planta.jpg'))
im = np.array(Image.open('planta.jpg').convert('L'))

#Visualizando com Matiplotlib
import matplotlib.pyplot as plt
from skimage.filters import roberts, sobel
from skimage.morphology import disk
from skimage.filter.rank import entropy
ent = entropy(im, disk(5))

imRoberts = roberts(im)
imSobel = sobel(im) 

fig, (ax0, ax1) = plt.subplots(ncols=2)
fig.suptitle('Minicurso Image Processing')

ax0.imshow(im, cmap=plt.cm.gray)
ax0.set_title('Imagem com cor')

ax1.imshow(ent, cmap=plt.cm.gray)
ax1.set_title('Imagem sem cor')

plt.show()











