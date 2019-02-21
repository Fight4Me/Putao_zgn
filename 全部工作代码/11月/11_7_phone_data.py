# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 15:12:04 2018

@author: bnuzgn
"""
import re
import os
import time
import json

def pre_process(text):
    pattern_1 = re.compile('\.|—|:|\||,|!|\?')
    text.strip()
    text = re.sub(pattern_1,'',text)
    text = text.upper()
    text_list = text.split()
#    print(text)
    return len(text_list)

def get_wenben_list(text):
    pattern_1 = re.compile('\.|—|:|\||,|!|\?')
    text.strip()
    text = re.sub(pattern_1,'',text)
    text = text.upper()
    wenben_list = text.split()
#    print(text_list)
    return wenben_list

def json_process(text_length,text_list,wenben_list):
    dic2 = {}      
    pattern_1 = re.compile('^(.*?):')
    pattern_2 = re.compile('\((.*?)\)')
    pattern_3 = re.compile('\)(.*)')
    """前三个正则表达式用于分割开文本，音标和音素，后两个用于获得其余信息"""
    pattern_6 = re.compile('\d')
    pattern_4 = re.compile('[\^\$]')
    pattern_5 = re.compile('^(.*?)\d[\^\$]$')
    pattern_7 = re.compile('^(.*?)\d$')
    pattern_8 = re.compile('^(.*?)[\^\$]$')
    print(text_list)
    for k in range(0,text_length): 
        dic = {}
        i = k+3
        json_list = []
        text = text_list[i]
        number_list = []
        condition_list = []
        word_judge = '0'
        wenben = pattern_1.findall(text)[0].strip().upper()
        try:
            yinbiao = pattern_2.findall(text)[0].strip().split()
            yinsu = pattern_3.findall(text)[0].strip().split()
            for j in range(0,len(yinsu)):
                if re.match(pattern_4,yinsu[j][-1]) and re.match(pattern_6,yinsu[j][-2]):
                    number = yinsu[j][-2]
                    if yinsu[j][-1] == '^':
                        condition_list.append('1')
                    elif yinsu[j][-1] == '$':
                        condition_list.append('2')
                    yinsu[j] = pattern_5.findall(yinsu[j])[0]
                elif re.match(pattern_6,yinsu[j][-1]):
                    number = yinsu[j][-1]
                    yinsu[j] = pattern_7.findall(yinsu[j])[0]
                    condition_list.append('0')
                elif re.match(pattern_4,yinsu[j][-1]):
                    number = '-1'
                    if yinsu[j][-1] == '^':
                        condition_list.append('1')
                    elif yinsu[j][-1] == '$':
                        condition_list.append('2')
                    yinsu[j] = pattern_8.findall(yinsu[j])[0]
                else:
                    number = '-1'
                    condition_list.append('0')
                number_list.append(number)
        except:
            yinbiao = []
            yinsu = []
            number_list = []
            condition_list = []
        json_list.append(yinbiao)
        json_list.append(yinsu)
        json_list.append(number_list)
        json_list.append(condition_list)
        json_list.append(word_judge)
#        print(json_list)
#        print(yinbiao)
#        print(yinsu)
#        print(k)
        dic.update({wenben:json_list})
        wenben_list[k]= dic
    dic2.update({'words':wenben_list})
    dic2.update({'sentence':'0'})
    wenben_json = json.dumps(dic2)
    return wenben_json
#    print(dic)
        

if __name__ == '__main__':
    file_path = r'C:\Users\bnuzgn\Desktop\putao\11_7\sentence.txt'
    save_path = r'C:\Users\bnuzgn\Desktop\putao\11_7\sentence_process3.txt'
    with open(file_path,'r',encoding = 'utf-8')as f:
        text_lines = f.readlines()
        string = 'audio_name'+'\t'+'text'+'\t'+'task_id'+'\t'+'phone_text\n'
        for line in text_lines:
            line = line.strip()
            text_list = line.split('\t')
            name = text_list[1]
            raw_text = text_list[2]
            text_length = pre_process(raw_text)
            wenben_list = get_wenben_list(raw_text)
            wenben_json = json_process(text_length,text_list,wenben_list)
            string = string+name+'\t'+raw_text+'\t'+'935'+'\t'+wenben_json+'\n'
#    print(string)
    with open(save_path,'w',encoding = 'utf-8')as f:
        f.write(string)
            
            