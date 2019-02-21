# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 18:40:41 2018

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

train_path = r'C:\Users\bnuzgn\Desktop\putao\10_18\train'
test_path = r'C:\Users\bnuzgn\Desktop\putao\10_18\test'
test2_path = r'C:\Users\bnuzgn\Desktop\putao\10_18\test2'
test3_path = r'C:\Users\bnuzgn\Desktop\putao\10_18\test3'
test4_path = r'C:\Users\bnuzgn\Desktop\putao\10_18\test4'

train_x = np.loadtxt(train_path, usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15) , dtype='float' , skiprows=1)
train_y = np.loadtxt(train_path, usecols=0 , dtype='float' , skiprows=1)
test_x = np.loadtxt(test_path, usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15) , dtype='float' , skiprows=1)
test_y = np.loadtxt(test_path, usecols=0 , dtype='float' , skiprows=1)
test_x2 = np.loadtxt(test2_path, usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15) , dtype='float' , skiprows=1)
test_y2 = np.loadtxt(test2_path, usecols=0 , dtype='float' , skiprows=1)
test_x3 = np.loadtxt(test3_path, usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15) , dtype='float' , skiprows=1)
test_y3 = np.loadtxt(test3_path, usecols=0 , dtype='float' , skiprows=1)
test_x4 = np.loadtxt(test4_path, usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15) , dtype='float' , skiprows=1)
test_y4 = np.loadtxt(test4_path, usecols=0 , dtype='float' , skiprows=1)

scaler = preprocessing.minmax_scale(train_x)
clf = GradientBoostingClassifier(random_state=10)

#clf.fit(train_x,train_y)
#pred_y = clf.predict(test_x)
#print(classification_report(test_y,pred_y))
##print((test_y.tolist()[0]))
#print("accuracy_score\t"+str(accuracy_score(test_y.tolist(), pred_y.tolist())))
#
#clf.fit(train_x,train_y)
#pred_y = clf.predict(test_x2)
##print(pred_y)
#print(classification_report(test_y2,pred_y))
#print("accuracy_score\t"+str(accuracy_score(test_y2.tolist(), pred_y.tolist())))
#
#clf.fit(train_x,train_y)
#pred_y = clf.predict(test_x3)
#print(classification_report(test_y3,pred_y))
#print("accuracy_score\t"+str(accuracy_score(test_y3.tolist(), pred_y.tolist())))

clf.fit(train_x,train_y)
pred_y = clf.predict(test_x4)
print(classification_report(test_y4,pred_y))
print("accuracy_score\t"+str(accuracy_score(test_y4.tolist(), pred_y.tolist())))