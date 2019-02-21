# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 11:38:01 2018

@author: bnuzgn
"""
import re
import os
import time
import json

def pre_process(line):
    pattern_1 = re.compile('^(.*?):')
    line = line.strip()
    text_list = line.split('\t')
    raw_text = text_list[2]
    pattern_1 = re.compile('\.|—|:|\||,|!|\?')
    raw_text.strip()
    raw_text = re.sub(pattern_1,'',raw_text)
    raw_text = raw_text.upper()
    text_list = raw_text.split()
    print(text_list)
    return len(text_list)

#def get_newLine(line,length):
#    line = line.strip()
#    text_list = line.split('\t')
#    for 

if __name__ == '__main__':
    file_path_A = r'C:\Users\bnuzgn\Desktop\putao\11_12\txt_w_A.txt'
    file_path_H = r'C:\Users\bnuzgn\Desktop\putao\11_12\txt_w_H.txt'
    file_path_O = r'C:\Users\bnuzgn\Desktop\putao\11_12\txt_w_O.txt'
    save_path = r'C:\Users\bnuzgn\Desktop\putao\11_12\word_gather.txt'
    
    total_str = ''
    with open(file_path_A,'r',encoding = 'utf-8')as f1,open(file_path_H,'r',encoding = 'utf-8')as f2,open(file_path_O,'r',encoding = 'utf-8')as f3:
        try:
            while True:
                A_text_line = f1.readline()
                H_text_line = f2.readline()
                O_text_line = f3.readline()
                A_length = pre_process(A_text_line)
                H_length = pre_process(H_text_line)
                O_length = pre_process(O_text_line)
                if A_text_line and H_text_line and O_text_line:
                    total_str = total_str+A_text_line+H_text_line+O_text_line
                else:
                    break
        except:
            pass
            
#        for line in A_text_lines:
#            line = line.strip()
#            text_list = line.split('\t')
#            name = text_list[1]
#            raw_text = text_list[2]
#            text_length = pre_process(raw_text)
#            wenben_list = get_wenben_list(raw_text)
#            wenben_json = json_process(text_length,text_list,wenben_list)
#            string = string+name+'\t'+raw_text+'\t'+wenben_json+'\n'
##    print(string)
    with open(save_path,'w',encoding = 'utf-8')as f1:
        f1.write(total_str)