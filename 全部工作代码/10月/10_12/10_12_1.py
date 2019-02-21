# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 10:40:54 2018

@author: bnuzgn
"""
import re

def normal_word_leven(str1, str2):
    str1 = re.sub('[\.,!\?]','',str1).lower().strip().split()
    str2 = re.sub('[\.,!\?]','',str2).lower().strip().split()
    print(str1 , str2)
    len_str1 = len(str1) + 1
    len_str2 = len(str2) + 1
    matrix = [0 for n in range(len_str1 * len_str2)]
    for i in range(len_str1):
      matrix[i] = i
    for j in range(0, len(matrix), len_str1):
      if j % len_str1 == 0:
        matrix[j] = j // len_str1
    for i in range(1, len_str1):
      for j in range(1, len_str2):
        if str1[i-1] == str2[j-1]:
          cost = 0
        else:
          cost = 1
        matrix[j*len_str1+i] = min(matrix[(j-1)*len_str1+i]+1,
                      matrix[j*len_str1+(i-1)]+1,
                      matrix[(j-1)*len_str1+(i-1)] + cost)
    return 100-matrix[-1]


str1 = r'Dog! This is a dog'
str2 = r'Dog!!! this is a dog'
test = normal_word_leven(str1,str2)
print(test)