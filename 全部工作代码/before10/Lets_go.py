# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 10:23:07 2018

@author: bnuzgn
"""

import os
import re
from Sentense import contain_zh
from count import count_file

judge_pattern=re.compile('.*?[.!?]$')

'''
根据Let‘s go的特征选择的句子特征
'''
def Judge(line):
    if judge_pattern.search(line):
        return True
    else:
        return False

filePath=r'C:\Users\bnuzgn\Desktop\LetsGO\Text'
outPath=r'C:\Users\bnuzgn\Desktop\LetsGO\Process'

list_1 =os.listdir(filePath)
for i in range(0,len(list_1)):
#    print(list_1[i])
    sub_dir_path=os.path.join(filePath,list_1[i])#子目录路径
    list_2=os.listdir(sub_dir_path)
    for j in range(0,len(list_2)):
#        print(list_2[j])
        file_path=os.path.join(sub_dir_path,list_2[j])  #文本路径
        out_file_path=os.path.join(outPath,list_1[i],list_2[j]) #输出文件路径
        print(out_file_path)
#        print(file_path)
        sentense=''
        with open(file_path) as f:
#            print(f.read())
            for line in f.readlines():
                if (not contain_zh(line)) and Judge(line):
                    line = re.sub('^[a-zA-Z\d]\.','',line)
                    line = re.sub('^\d ','',line)
#                    print(line)
                    sentense=sentense+line
        with open(out_file_path,'w') as f:
            f.write(sentense)


                    