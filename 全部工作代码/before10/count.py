# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import re

file_path=r'C:\Users\bnuzgn\Desktop\WebSpider\storiestogrowby\Text'
global count
count=0

def count_file(file_path): 
    global count
    try:
        with open(file_path,encoding='utf-8')as f:
            readline=f.readlines()
            for line in readline:
    #                print(line)
                line=re.sub('(^A:)|(^B:)|\.|—|:|\||,|!|\?','',line)
    #                print(line)
                wo=line.split()
                word.extend(wo)
    #                print(len(word))
            count=count+len(word)
    except:
        with open(file_path)as f:
            readline=f.readlines()  
            for line in readline:
    #                print(line)
                line=re.sub('(^A:)|(^B:)|\.|—|:|\||,|!|\?','',line)
    #                print(line)
                wo=line.split()
                word.extend(wo)
    #                print(len(word))
            count=count+len(word)
    print(count)
    

list1 =os.listdir(file_path) 

for i in range(0,len(list1)):
    word=[]
    filepath = os.path.join(file_path,list1[i])  
    count_file(filepath)
#for i in range(0,len(list1)):
#    sub_path = os.path.join(file_path,list1[i])  
#    list2 =os.listdir(sub_path) 
#    for j in range(0,len(list2)):
#        '''
#        word这个词汇需要根据情况进行变化
#        '''
#        word=[]
#        filepath=os.path.join(sub_path,list2[j])
#        count_file(filepath)