#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 16:30:20 2019

@author: george
"""
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 30 14:55:02 2018

@author: George Oliveira Barros, george_gob@hotmail.com. 

KNN Classification: Ferrugem em folhas de Soja
"""

print __doc__
from sklearn.neighbors import KNeighborsClassifier
from sklearn import cross_validation, metrics
#from sklearn.metrics import classification_report, confusion_matrix, mean_squared_error
import numpy as np
from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier

dataset = [[1,	0.0204636,	0.0133376,	0.00953688,	0.00341483, 	0.00164136,	0.00907769],
[1,	0.00669575,	0.0106814,	0.00774814,	0.00890814,	0.00821537,	0.0100264],
[1,	0.00690593,	0.0101678,	0.00904687,	0.00659567,	0.0077139,	0.00898189],
[1, 	0.00659859,	0.00741664,	0.00995447,	0.00698596,	0.0090852,	0.00627016],
[1,	0.00912523,	0.00658927,	0.00228592,	0.0114712,	0.00651312,	0.00510995],
[1,	0.00827189,	0.0107559,	0.00925111,	0.0117198,	0.00981794,	0.00672559],
[1,	0.00981018,	0.0109512,	0.00974555,	0.00829709,	0.00690409,	0.00708107],
[1,	0.0058237,	0.0113777,	0.00644452,	0.00499253,	0.0122244,	0.0108903],
[1,	0.0109513,	0.00747111,	0.00539619,	0.0174862,	0.00418875,	0.00847688],
[1,	0.0319101,	0.00713714,	0.00782408,	0.00553952,	0.00798662,	0.0132618],
[1,	0.00549979,	0.00689684,	0.00648652,	0.00591182,	0.0116031,	0.0133263],
[1,	0.0135024,	0.00320415,	0.00803458,	0.00523355,	0.0110031,	0.00867735],
[1,	0.0102584,	0.00555783,	0.00975169,	0.00652213,	0.0183783,	0.014814],	
[1,	0.00910255,	0.0105504,	0.0087104,	0.0119906,	0.0126325,	0.00819531],
[1,	0.0051387,	0.0121267,	0.00545138,	0.0112118,	0.00136324,	0.0112442],
[1,	0.00917427,	0.00767379,	0.00908069,	0.00601052,	0.00688498,	0.0156074],
[1,	0.00580846,	0.00524826,	0.00800738,	0.0103604,	0.00853933,	0.00837615],
[1,	0.00359148,	0.011669,	0.00817398,	0.0109256,	0.00964643,	0.00912934],	
[1,	0.0119482,	0.00338181,	0.00716805,	0.0120872,	0.0128578,	0.00783182],
[1,	0.00815155,	0.00857564,	0.00654278,	0.0103689,	0.00267941,	0.0168731],
[0,	0.0101969,	0.00585266,	0.0074627,	0.0108725,	0.00951896,	0.00873355],
[0,	0.00603126,	0.0106133,	0.0113276,	0.00791521,	0.00964026,	0.0128737],
[0,	0.00840709,	0.00628094,	0.00913717,	0.00830687,	0.00881683,	0.0110384],
[0,	0.00936484,	0.00961701,	0.0100994,	0.00993234,	0.00977282,	0.00818223],
[0,	0.00876215,	0.00746074,	0.00883896,	0.00808382,	0.00735442,	0.00910983],
[0,	0.00755109,	0.00840835,	0.00706052,	0.00711739,	0.00817878,	0.00782358],
[0,	0.0106911,	0.008299,	0.0110317,	0.0128043,	0.00776525,	0.0109298],
[0,	0.0038133,	0.00864806,	0.0090975,	0.00720055,	0.0100012,	0.00803463],
[0,	0.00971464,	0.0124419,	0.00867487,	0.00762533,	0.00795941,	0.0102974],
[0,	0.0105618,	0.011505,	0.00956331,	0.00217191,	0.0108237,	0.011001],
[0,	0.00377948,	0.00785576,	0.00794465,	0.010642,	0.00831435,	0.00991933],
[0,	0.00972494,	0.00915713,	0.0115417,	0.0121637,	0.0134747,	0.00957601],
[0,	0.00721411,	0.00988293,	0.0104331,	0.0122019,	0.013711,	0.0108306],
[0,	0.0109388,	0.0126779,	0.012505,	0.0113162,	0.0115602,	0.00979985],
[0,	0.00983408,	0.00899329,	0.0115261,	0.00827783,	0.00881143,	0.00859272],
[0,	0.00810562,	0.00928873,	0.0109321,	0.0093175,	0.0091218,	0.00965614],
[0,	0.0119823,	0.0104875,	0.0107457,	0.0080951,	0.0092087,	0.00865887],
[0,	0.0125769,	0.0105518,	0.0128158,	0.0118814,	0.00896609,	0.01099],
[0,	0.00936484,	0.00961701,	0.0100994,	0.00993234,	0.00977282,	0.00818223],	
[0,	0.00840709,	0.00628094,	0.00913717,	0.00830687,	0.00881683,	0.0110384]]
dataset = np.array(dataset)

#Preparando o dataset
number_feats = 6
y = dataset[:,0]
X = dataset[:,1:7]
    

#Selecionando conjunto de validação (10% das amostras) -> 4 amostras
validation_X = np.ones((4, number_feats))
validation_y = np.ones((4))

#primeiro as amostras com ferrugem (2 amostras)
validation_X[0:2,:] = X[0:2,:]
validation_y[0:2] = y[0:2]

#Por fim, as amostras sem ferrugem (2 amostras)
validation_X[2:4,:] = X[38:40,:]
validation_y[2:4] = y[38:40]
#Separando o conjunto pro CROSS VALIDATION (90% restante)
X = X[2:38,:]
y = y[2:38]


fold = 4

n_neighbors=1
classif = OneVsRestClassifier(estimator=SVC(gamma='scale',random_state=0))
neigh = classif
#neigh = KNeighborsClassifier(n_neighbors, weights='uniform', algorithm='auto',  p=1) #KNN = 9 -> Melhor resultado
k_fold = cross_validation.StratifiedKFold(y, fold) #Cross Validation K-fold = 10 and KNN
accFinal = 0
prec = 0
rec = 0



print "=========================================="
print "KNN + Cross Validation 10-fold"
print "=========================================="
for k, (train, test) in enumerate(k_fold):
    neigh.fit(X[train], y[train])
    acc = neigh.score(X[test], y[test])
    y_predict = neigh.predict(X[test])
    print("fold",k, "-> score:", acc )
    #print("-> precision:", metrics.precision_score(y[test], y_predict))
    #print("-> recall:", metrics.recall_score(y[test], y_predict))
    accFinal += acc
    prec +=  metrics.precision_score(y[test], y_predict)
    rec += metrics.recall_score(y[test], y_predict)
      
accFinal = accFinal/(k+1); accfim = accFinal;
rec = rec/(k+1)
prec = prec/(k+1)
error_rate = 1 - accFinal

print "KNN Classification: k=",n_neighbors
print "Generalization Set: Accuracy =", accfim ,"%"
print "Precision:", prec
print "Recall:",rec
print "========================================================================"
neigh.fit(X, y) #New training with generalization set
print "Validation Set: Accuracy =", neigh.score(validation_X, validation_y) ,"%" 
y_predict = neigh.predict(validation_X)
print("Precision:", metrics.precision_score(validation_y, y_predict))
print("Recall:", metrics.recall_score(validation_y, y_predict))