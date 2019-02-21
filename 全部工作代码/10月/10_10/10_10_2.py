# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 15:18:05 2018

@author: bnuzgn
"""
import xlrd 
import json
import time
import os
import re
from xlutils.copy import copy

read_path=r'C:\Users\bnuzgn\Desktop\60_80_label_new.xls'
save_path=r'C:\Users\bnuzgn\Desktop\60_80_label_new2.xls'

excel_read = xlrd.open_workbook(read_path)
if __name__=='__main__':
    excel_save = xlrd.open_workbook(save_path)
    excel_save_copy = copy(excel_save)
    sheet_save = excel_save_copy.get_sheet(0)
    sheet = excel_read.sheets()[0]  #获取Excel文件中的第一页表单
    texts = sheet.col_values(2)
#    print(texts)
#    print(len(texts))
    fluency = 0
    integrity = 0
    pronunciation = 0
    score = 0
    for number in range(1,2001):
        words_score = ""
        word_json = json.loads(texts[number])
        fluency = word_json["lines"][0]["fluency"]
        integrity = word_json["lines"][0]["integrity"]
        pronunciation = word_json["lines"][0]["pronunciation"]
        score = word_json["lines"][0]["score"]
#        print(word_json['lines'])
#        time.sleep(4)
        words_list = word_json["lines"][0]["words"]
        length = len(words_list)
        for i in words_list:
            words_score = str(i["score"])+','+words_score
        words_score = re.sub(',$','',words_score)
#        print(words_score)
#        time.sleep(2)
        sheet_save.write(number, 3, fluency)
        sheet_save.write(number, 4, integrity)
        sheet_save.write(number, 5, pronunciation)
        sheet_save.write(number, 6, score)
        sheet_save.write(number, 7, words_score)
    excel_save_copy.save(save_path)