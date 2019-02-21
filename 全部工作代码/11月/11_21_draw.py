# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 11:03:30 2018

@author: bnuzgn
"""
import os

file_path = r'C:\Users\bnuzgn\Desktop\stat.txt'
file_path2 = r'C:\Users\bnuzgn\Desktop\stat2.txt'
col1 = []
col2 = []

with open(file_path2,'r',encoding='utf-8')as f:
    lines = f.readlines()
    for line in lines:
        col1.append(line.strip().split()[0])
        col2.append(line.strip().split()[1])
        
print(col2)