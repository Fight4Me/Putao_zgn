# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 14:22:58 2018

@author: bnuzgn
"""
import json
import time
import os
import re

def normal_leven(str1, str2):
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

save_path = r'C:\Users\bnuzgn\Desktop\10_12\new3.txt'

pattern_1 = re.compile('^[^\.].*\.txt')
pattern_2 = re.compile('res_weixin_asr')
pattern_3 = re.compile('res_weixin_ise_s')
pattern_4 = re.compile('[\.,!\?]')
pattern_5 = re.compile('res_xunfei_asr')

xf_test1 = r'A boy!'
raw_test2 = r'throw a ball.'

xf_test1 = re.sub('[\.,!\?]','',xf_test1).lower().strip()
raw_test2 = re.sub('[\.,!\?]','',raw_test2).lower().strip()

out_put = ""
out_put=out_put+'num'+'\t'+str('wx_num')+'\t'+str('wx_accuracy')+'\t'+str('wx_completion')+'\t'+str('wx_fluency')+'\t'+str('wx_min')+'\t'+str('wx_max')+'\t'+str('wx_avg')+'\t'+str('wx_more')+'\t'+str('wx_less')+'\t'+'xf_leven''\n'

with open(r'C:\Users\bnuzgn\Desktop\new.json') as f:
    te = f.read()
ise_json = json.loads(te)
num = len(raw_test2.split())
#    wx_leven = normal_leven(raw_text, asr_text)
xf_leven = normal_leven(xf_test1, raw_test2)
wx_num = len(ise_json['words'])
#print(raw_text,"|||",xf_asr_text,"|||",asr_text)
wx_accuracy = ise_json['pron_accuracy']
wx_completion = ise_json['pron_completion']
wx_fluency = ise_json['pron_fluency']
wx_words_list = ise_json['words']
wx_more = 0
wx_less = 0
wx_min = 100
wx_max = -1
tag_0 = 0
total = 0
for word_dic in wx_words_list:
    tag = word_dic["tag"]
    word = word_dic["word"]
    pron_accuracy = word_dic["pron_accuracy"]
    if tag == 1:
        wx_more = wx_more+1
    if tag == 2:
        wx_less = wx_less+1
    if tag == 0:
        tag_0 = tag_0+1
        wx_min = min(pron_accuracy,wx_min)
        wx_max = max(pron_accuracy,wx_max)
        total = total + pron_accuracy
wx_avg = total/tag_0
out_put=out_put+str(num)+'\t'+str(wx_num)+'\t'+str(wx_accuracy)+'\t'+str(wx_completion)+'\t'+str(wx_fluency)+'\t'+str(wx_min)+'\t'+str(wx_max)+'\t'+str(wx_avg)+'\t'+str(wx_more)+'\t'+str(wx_less)+'\t'+str(xf_leven)+'\n'
with open(save_path,'w',encoding='utf-8')as f5:
    f5.write(out_put)