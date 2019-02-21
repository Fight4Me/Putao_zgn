# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 18:58:32 2018

@author: bnuzgn
"""

import numpy as np
from sklearn.svm import SVC
from sklearn import preprocessing
from sklearn.metrics import classification_report,accuracy_score,f1_score
from sklearn.model_selection  import train_test_split

filePath = r'C:\Users\bnuzgn\Desktop\2018-12-20.feat'
train_x = np.loadtxt(filePath,delimiter='\t', usecols=(0,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30) , dtype='float' , skiprows=1)
#train_x = np.loadtxt(filePath,delimiter='\t', usecols=(0,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30) , dtype='float' , skiprows=1)
train_y =  np.loadtxt(filePath,delimiter='\t', usecols=2, dtype='float' , skiprows=1)
X_train,X_test, y_train, y_test =train_test_split(train_x,train_y,test_size=0.2, random_state=10)
scaler = preprocessing.minmax_scale(X_train)
clf = SVC(kernel='rbf',C=10)
clf.fit(X_train,y_train)
pred_y = clf.predict(X_test)
print(classification_report(y_test,pred_y))
print("accuracy_score\t"+str(accuracy_score(y_test.tolist(), pred_y.tolist())))
