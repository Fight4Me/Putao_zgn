# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 09:47:56 2018

@author: bnuzgn
"""
import os 
import re
import json

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

read_path = r'C:\Users\bnuzgn\Desktop\10_10\operate.txt'
save_path = r'C:\Users\bnuzgn\Desktop\10_10\out_put.txt'
check_path = r'C:\Users\bnuzgn\Desktop\10_10\weixin_sentence'
pattern_1 = re.compile('\d+')

if __name__ == '__main__' :
    with open(read_path,encoding='utf-8')as f:
        read_lines=f.readlines()
        out_put = ""
        out_put=out_put+'label'+'\t'+'num'+'\t'+str('wx_num')+'\t'+str('wx_accuracy')+'\t'+str('wx_completion')+'\t'+str('wx_fluency')+'\t'+str('wx_min')+'\t'+str('wx_max')+'\t'+str('wx_avg')+'\t'+str('wx_more')+'\t'+str('wx_less')+'\t'+str('wx_leven')+'\t'+str('xf_leven')+'\n'
        for line in read_lines:
#            print(line)
            list1=line.strip().split('\t')
#            print(len(list1))
            label=list1[0]
            each_line_file_path = os.path.join(check_path,list1[9],list1[10],'res_weixin_ise_s')
            wx_more = 0
            wx_less = 0
#            print(each_line_file_path)       

            num=len(re.sub(pattern_1,'',list1[9]).split())
#            print(num)
            wx_words_list = list1[6].split(',') #微信每个词的打分的string值
            wx_num = len(wx_words_list)
#            if wx_num != len(wx_word_list):
#                print(each_line_file_path)
#                print("2333")
#            print(wx_num)
            wx_accuracy = list1[3]
#            print(wx_accuracy)
            wx_completion = list1[4]
            wx_fluency = list1[5]
        
            with open(each_line_file_path,encoding='utf-8')as f2:
#                print(f2.read())
                wx_json = json.loads(f2.read())
#                print(wx_json["words"])
                wx_judge = wx_json["ret"]
                if wx_judge != 0 :
#                    print("2333")
                    continue
                wx_word_list=wx_json["words"]
#                print(wx_word_list)
#                print(len(wx_word_list))
                wx_min=100
                wx_max=-1
                tag_0 = 0
                total = 0
                for word_dic in wx_word_list:
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
#                print(wx_min,wx_max,total,wx_avg)
#                xf_asr_text = xf_asr_text.translate(None,string.punctuation)
                xf_sentence = re.sub('[\.,!\?]','',str(list1[7])).lower()
                wx_sentence = re.sub('[\.,!\?]','',str(list1[8])).lower()
                origin_sentence = re.sub('[\.,!\?]','',str(re.sub(pattern_1,'',list1[9]))).lower()
#                print(wx_sentence,origin_sentence)
                wx_leven = normal_leven(wx_sentence,origin_sentence)
                xf_leven = normal_leven(xf_sentence,origin_sentence)
                
                out_put=out_put+str(label)+'\t'+str(num)+'\t'+str(wx_num)+'\t'+str(wx_accuracy)+'\t'+str(wx_completion)+'\t'+str(wx_fluency)+'\t'+str(wx_min)+'\t'+str(wx_max)+'\t'+str(wx_avg)+'\t'+str(wx_more)+'\t'+str(wx_less)+'\t'+str(wx_leven)+'\t'+str(xf_leven)+'\n'
            with open(save_path,'w',encoding='utf-8')as f3:
                f3.write(out_put)