# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 09:49:51 2018

@author: bnuzgn
"""
import xlrd 
import os 
import re
import json
import time
from selenium import webdriver 
from xlutils.copy import copy

homepage=r'https://demo-edu.hivoice.cn:12000/'
read_path = r'C:\Users\bnuzgn\Desktop\10_10\operate2.txt'
save_path = r'C:\Users\bnuzgn\Desktop\10_10\save.xls'
check_path = r'C:\Users\bnuzgn\Desktop\10_10\hyf_data_res\sentence'

if __name__ == '__main__' :
    line_count = 0
    excel_save = xlrd.open_workbook(save_path)
    excel_save_copy = copy(excel_save)
    sheet_save = excel_save_copy.get_sheet(0)
    browser = webdriver.Chrome()
    browser.get(homepage)
    browser.find_element_by_css_selector('#useFlash').click()
    browser.find_element_by_css_selector('#init').click()
    time.sleep(40)
    pattern = re.compile('.*评测结果:',re.S)
    with open(read_path,encoding='utf-8')as f:
        read_lines=f.readlines()
        for line in read_lines:
            try:
                line_count = line_count + 1
                if line_count >= 0:
                    list1=line.strip().split('\t')
                    each_folder_path = os.path.join(check_path,list1[0],list1[1])
                    list2 =os.listdir(each_folder_path)
                    for file_name in list2:
                        if(re.search('^[^\.].*\.mp3$',file_name)):
                            mp3_path = os.path.join(each_folder_path,file_name)
#                                if not os.path.exists(mp3_path):
#                                    print(mp3_path)
                        elif (re.search('^[^\.].*\.txt$',file_name)):
                            txt_path = os.path.join(each_folder_path,file_name)
#                                if not os.path.exists(txt_path):
#                                    print(txt_path)
                            with open(txt_path,encoding='utf-8') as f2:
                                text = f2.read()
                    browser.find_element_by_css_selector('#useFlash').click()
                    browser.find_element_by_css_selector('#init').click()
                    browser.find_element_by_css_selector('#text').clear()
                    browser.find_element_by_css_selector('#text').send_keys(text)
                    browser.find_element_by_css_selector('#file').send_keys(mp3_path)
                    time.sleep(2)
                    browser.find_element_by_css_selector('#eval').click()
                    time.sleep(2)
                    json_text=browser.find_element_by_css_selector('#result').text
                    json_text=re.sub(pattern,'',json_text)
                    word_json = json.loads(json_text)
                    fluency = word_json["lines"][0]["fluency"]
                    integrity = word_json["lines"][0]["integrity"]
                    pronunciation = word_json["lines"][0]["pronunciation"]
                    score = word_json["lines"][0]["score"]
                    words_list = word_json["lines"][0]["words"]
                    length = len(words_list)
                    words_score = ""
                    for i in words_list:
                        words_score = str(i["score"])+','+words_score
                    words_score = re.sub(',$','',words_score)
#                    print(json_text)
#                    sheet_save.write(line_count,0, json_text)
                    sheet_save.write(line_count, 3, fluency)
                    sheet_save.write(line_count, 4, integrity)
                    sheet_save.write(line_count, 5, pronunciation)
                    sheet_save.write(line_count, 6, score)
                    sheet_save.write(line_count, 7, words_score)
            except Exception as e:
                print(line_count)
                print(e)
                browser.quit()
                excel_save_copy.save(save_path)
                break
        excel_save_copy.save(save_path) 
    browser.quit()