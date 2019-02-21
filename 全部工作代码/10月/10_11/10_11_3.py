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

index_path = r'C:\Users\bnuzgn\Desktop\10_11\samples_res'
save_path = r'C:\Users\bnuzgn\Desktop\10_11\test2.txt'
pattern_1 = re.compile('^[^\.].*\.txt')
pattern_2 = re.compile('res_weixin_asr')
pattern_3 = re.compile('res_weixin_ise_s')
pattern_4 = re.compile('[\.,!\?]')
pattern_5 = re.compile('res_xunfei_asr')

out_put = ""
out_put=out_put+'dir_name'+'\t'+'num'+'\t'+str('wx_num')+'\t'+str('wx_accuracy')+'\t'+str('wx_completion')+'\t'+str('wx_fluency')+'\t'+str('wx_min')+'\t'+str('wx_max')+'\t'+str('wx_avg')+'\t'+str('wx_more')+'\t'+str('wx_less')+'\t'+str('wx_leven')+'\t'+'xf_leven''\n'

list1 = os.listdir(index_path)
for each_1 in list1:
    dir_name = each_1
    check_path_2 = os.path.join(index_path,each_1)
    list2 = os.listdir(check_path_2)
    for each_2 in list2:
        if re.search(pattern_1, each_2):
            txt_path = os.path.join(index_path,each_1,each_2)
            with open(txt_path, encoding = 'utf-8') as f1:
                raw_text = f1.read()
                raw_text = re.sub('[\.,!\?]','',raw_text).lower().strip()
        elif re.search(pattern_2, each_2):
            asr_path = os.path.join(index_path,each_1,each_2)
            with open(asr_path , encoding = 'utf-8') as f2:
                asr_json_text = f2.read().strip()
                asr_json = json.loads(asr_json_text)
        elif re.search(pattern_5, each_2):
            asr_path = os.path.join(index_path,each_1,each_2)
            with open(asr_path , encoding = 'utf-8') as f3:
                xf_asr_text = f3.read()
                xf_asr_text = re.sub('[\.,!\?]','',xf_asr_text).lower().strip()
#                print(xf_asr_text)
        elif re.search(pattern_3, each_2):
            ise_path = os.path.join(index_path,each_1,each_2)
            with open(ise_path , encoding = 'utf-8') as f4:
                ise_json_text = f4.read()
                ise_json = json.loads(ise_json_text) 
        '''已经完成所有的原始文件的读入与保存'''
    if ise_json['ret'] != 0:
        continue
    num = len(re.sub(pattern_4,'',raw_text).split())
    asr_text = asr_json['res']['sentences'][0]['text']
    asr_text = re.sub('[\.,!\?]','',asr_text).lower()
    wx_leven = normal_leven(raw_text, asr_text)
    xf_leven = normal_leven(raw_text, xf_asr_text)
    wx_num = len(ise_json['words'])
    print(raw_text,"|||",xf_asr_text,"|||",asr_text)
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
    out_put=out_put+dir_name+'\t'+str(num)+'\t'+str(wx_num)+'\t'+str(wx_accuracy)+'\t'+str(wx_completion)+'\t'+str(wx_fluency)+'\t'+str(wx_min)+'\t'+str(wx_max)+'\t'+str(wx_avg)+'\t'+str(wx_more)+'\t'+str(wx_less)+'\t'+str(wx_leven)+'\t'+str(xf_leven)+'\n'
    with open(save_path,'w',encoding='utf-8')as f5:
        f5.write(out_put)