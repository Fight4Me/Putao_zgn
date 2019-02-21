# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os

file_path=r'C:\Users\bnuzgn\Desktop\WebSpider\ForBeginners\Text'
global count
count=0

def read_file(file_path):
    global count
    list =os.listdir(file_path) 
    for i in range(0,len(list)):
        word=[]
        path = os.path.join(file_path,list[i])
#        print(path)
        with open(path,encoding='utf-8')as f:
            readline=f.readlines()
            for line in readline:
#                print(line)
                wo=line.split(' ')
                word.extend(wo)
#                print(len(word))
                count=count+len(word)
read_file(file_path)
print(count)