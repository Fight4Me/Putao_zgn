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
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn import naive_bayes
from sklearn import neighbors
from sklearn.neural_network import MLPClassifier

file_path = r'C:\Users\bnuzgn\Desktop\putao\10_17\new.txt'
save_path = r'C:\Users\bnuzgn\Desktop\putao\10_17\train_model.txt'

x = np.loadtxt(file_path, usecols=(1,2,3,4,5,6,7,8,9,10,11) , dtype='float' , skiprows=1)
y = np.loadtxt(file_path, usecols=0 , dtype='float' , skiprows=1)
#print(y)
scaler = preprocessing.minmax_scale(x)
#print(scaler)
train_x,test_x,train_y,test_y = train_test_split(x,y,test_size=0.8)

'''===================================================================='''

clf = SVC(kernel='linear',C=20)
clf.fit(train_x,train_y)
pred_y = clf.predict(test_x)
#print(classification_report(test_y,pred_y))
#joblib.dump(clf, save_path)
#print("num	wx_num	wx_accuracy	wx_completion	wx_fluency	wx_min	wx_max	wx_avg	wx_more	wx_less	xf_leven	xf_leven_word")
#print(clf.coef_)

clf = LogisticRegression()
clf.fit(train_x,train_y)
pred_y = clf.predict(test_x)
#print(classification_report(test_y,pred_y))

'''===================================================================='''

clf = naive_bayes.GaussianNB() # 高斯贝叶斯
clf = naive_bayes.MultinomialNB(alpha=1.0, fit_prior=True, class_prior=None)
clf = naive_bayes.BernoulliNB(alpha=1.0, binarize=0.0, fit_prior=True, class_prior=None)
clf.fit(train_x,train_y)
pred_y = clf.predict(test_x)
#print(classification_report(test_y,pred_y))

'''===================================================================='''

model = neighbors.KNeighborsClassifier(n_neighbors=5, n_jobs=1)
clf.fit(train_x,train_y)
pred_y = clf.predict(test_x)
#print(classification_report(test_y,pred_y))

'''===================================================================='''

model = MLPClassifier(activation='relu', solver='adam', alpha=0.0001)
clf.fit(train_x,train_y)
pred_y = clf.predict(test_x)
print(classification_report(test_y,pred_y))