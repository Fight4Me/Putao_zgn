# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 14:58:18 2018

@author: bnuzgn
"""
import os
import time
import re

dir_path = r'C:\Users\bnuzgn\Desktop\WebSpider\XinGaiNianYouth'
pattern_1 = re.compile('[A-Za-z]')
pattern_2 = re.compile('^\[.*\](.*?)$')

def delete(dirpath,filename):
    file_path = os.path.join(dirpath,filename)
    with open(file_path,'r',encoding = 'utf-8')as f :
        lines = f.readlines()
    new_text = ''
    for line in lines:
        line = line.strip()
        if line is not '':
            line = pattern_2.findall(line)[0]
            line = line.strip()
            if re.match(pattern_1,line[0]):
                new_text += line
                new_text += '\n'
    with open(file_path, 'w',encoding = 'utf-8') as f:
        f.write(new_text)

if __name__ =='__main__':
    for dirpath,dirnames,filenames in os.walk(dir_path):
        for filename in filenames:
            print(filename)
            delete(dirpath,filename)