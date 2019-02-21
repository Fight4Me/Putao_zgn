# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 13:41:15 2018

@author: bnuzgn
"""

import pickle
import numpy as np
from sklearn.svm import SVC
from sklearn.externals import joblib
from sklearn import preprocessing
from sklearn.model_selection  import train_test_split
from sklearn.metrics import classification_report,accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn import naive_bayes
from sklearn import neighbors
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier

train_path = r'C:\Users\bnuzgn\Desktop\putao\10_22\train.res'
train_x = np.loadtxt(train_path, usecols=(2,3,4) , dtype='float' )
train_y = np.loadtxt(train_path, usecols=0 , dtype='float')
#print(train_x)
train_x = preprocessing.minmax_scale(train_x)
X_train, X_test, y_train, y_test = train_test_split(train_x,train_y, test_size=0.8)


clf = LogisticRegression(penalty = 'l2', solver = 'liblinear',multi_class = 'auto')

clf.fit(X_train,y_train)
pred_y = clf.predict(X_test)
print(classification_report(y_test,pred_y))
print("accuracy_score\t"+str(accuracy_score(y_test.tolist(), pred_y.tolist())))
print (clf.coef_ ,clf.intercept_)