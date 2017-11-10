# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
"""
#Familiarizando com Python
print 'Olá mundo'
num1 = 8 
num2 = 8
soma = num1 + num2
print 'soma de',num1,'+',num2,'=',soma

lista = [10,2,3,4,5]
for i in lista:
    print i;
    
"""
    
#Numpy
import numpy as np

#Vetor
a = np.arange(24)
print a

#matriz
b = np.array([[0,1,2,3], [4,5,6,7], [8,9,10,111]])
print b

#Funções interessantes
#a.shape
#a.shape = (2,12)
#.size
#.dtype
#a.transpose()

#PIL pra ler imagens e converter
from PIL import Image
imRGB = np.array(Image.open('planta.jpg')) #imagem RGB
imGL = np.array(Image.open('planta.jpg').convert('L'))# Imagem em nível de cinza



               
#visualizando com Matiplotlib
import matplotlib.pyplot as plt

fig, (ax0, ax1) = plt.subplots(ncols=2)
fig.suptitle('Minicurso Image Processing - First Image Show')

ax0.imshow(imRGB, cmap=plt.cm.gray)
ax0.set_title('Imagem com cor')
ax0.axis('off')

ax1.imshow(imGL, cmap=plt.cm.gray)
ax1.set_title('Imagem sem cor')
ax1.axis('off')

plt.show()

#Vamos recortar  a imagem de depois visualizar novamente (Fatiamento)
#imGL = imGL[30:50,35:55]

#Criando arrays com numpy
#d = np.zeros( (2,4) )
#d = np.ones( (3,2,5), dtype=int16 )
#d = np.empty( (2,3), 'bool' )

#Fazendo uma matriz com reshape e manipulando linhas e colunas
#a = np.arange(20)
#a = a.reshape(4,5)

"""Exercísio das imagens, aplicar trnspose na planta e verificar resultado e recortar pedaço qualquer da planta"""

#sikit-image
#Teoria sobre filtros
#Depois prática com SKImage

#Reconhecendo Bordas
#from skimage.filter import roberts, sobel
#imRoberts = roberts(imGL)
#imSobel = sobel(imGL) 

#Entropia
#from skimage.morphology import disk
#from skimage.filter.rank import entropy
#ent = entropy(imGL, disk(5))

"""Exercício final: Busque na documentação do sikit-image os filtros disponíveis,
 crie um quadro com imagens a imagem original que você deseja  e o resultado da aplicação de 
 4 filtros diferentes. Apresente os resultados pra turma"""