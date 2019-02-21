# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 11:18:07 2018

@author: bnuzgn
"""
import os
import re
import time

file_path=r'C:\Users\bnuzgn\Desktop\WebSpider\Storynory_old\Text'
patthern=re.compile(r'Did')

list1 =os.listdir(file_path) 
for i in range(0,len(list1)):
    path = os.path.join(file_path,list1[i])   
    new_text=''
    with open(path,encoding='utf-8')as f:
        if 'Did' in str(f.read()):
            print(str(f.read()))
            time.sleep(1)