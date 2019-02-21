# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 12:12:38 2018

@author: bnuzgn
"""
import re 

zh_pattern = re.compile(u'[\u4e00-\u9fa5]+')

file_path=r'C:\Users\bnuzgn\Desktop\WebSpider\XinGaiNian.txt'

def Is_sentense(line):
    if re.search('[a-zA-Z]+\s[a-zA-Z]+',line):
        return True

def contain_zh(word):
    global zh_pattern
    match = zh_pattern.search(word)
    return match

if __name__ == '__main__':
    word1 = 'ceshi,测试'
    word2 = ' I live in a very old town which is surrounded by beautiful woods. It is a famous beauty spot. On Sundays, hundreds of people come from the city to see our town and to walk through the woods.'
    with open(file_path)as f:
        readline=f.readlines()
        for line in readline:
            if Is_sentense(line):
                if not contain_zh(line):
                    if r'Listen to the tape' not in line  and 'Lesson' not in line:
                        line=re.sub('\n','',line)
                        print(line)
#    if contain_zh(word1):
#        print ('%s 里面有中文' % word1)
#    if contain_zh(word2):
#        print ('%s 里面有中文' % word2)