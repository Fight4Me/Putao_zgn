# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 12:12:38 2018

@author: bnuzgn
"""
import re 

zh_pattern = re.compile(u'[\u4e00-\u9fa5]+')

file_path=r'C:\Users\bnuzgn\Desktop\WebSpider\XinGaiNian4.txt'
out_path=r'C:\Users\bnuzgn\Desktop\WebSpider\XinGaiNian4.txt'

def Is_sentense(line):
    if re.search('[a-zA-Z]+\s[a-zA-Z]+',line):
        return True

def contain_zh(word):
    global zh_pattern
    match = zh_pattern.search(word)
    return match

if __name__ == '__main__':
    new=''
    with open(file_path)as f:
        readline=f.readlines()
        for line in readline:
            if Is_sentense(line):
                if not contain_zh(line):
                    if r'Listen to the tape' not in line  and 'Lesson' not in line:
                        new=new+line
                        