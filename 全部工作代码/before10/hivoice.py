"""
Created on Tue Oct  2 15:57:02 2018

@author: 44128
"""

import xlrd 
import os
import re
import time
from selenium import webdriver 
from xlutils.copy import copy

browser = webdriver.Chrome()
file_path=r'C:\Users\bnuzgn\Desktop\60_80_new'
read_path=r'C:\Users\bnuzgn\Desktop\60_80_label.xlsx'
save_path=r'C:\Users\bnuzgn\Desktop\60_80_label_new.xls'
homepage=r'https://demo-edu.hivoice.cn:12000/'
excel_read = xlrd.open_workbook(read_path)

if __name__=='__main__':
    sheet = excel_read.sheets()[0]  #获取Excel文件中的第一页表单
    texts = sheet.col_values(1)
    list1 =os.listdir(file_path) 
    browser.get(homepage)
    browser.find_element_by_css_selector('#useFlash').click()
    browser.find_element_by_css_selector('#init').click()
    time.sleep(40)
    pattern = re.compile('.*评测结果:',re.S)
    for i in range(1,10):
        excel_save = xlrd.open_workbook(save_path)
        excel_save_copy = copy(excel_save)
        sheet_save = excel_save_copy.get_sheet(0)
        for number in range(1+i*200,201+i*200): 
            try:
    #        print(texts[number])
                for i in list1:
                    audio_number=re.sub(r'.mp3','',i)
                    if (audio_number == str(number)):
    #                    print(i)
                        audio_path = os.path.join(file_path,i)
                        browser.find_element_by_css_selector('#useFlash').click()
                        browser.find_element_by_css_selector('#init').click()
                        browser.find_element_by_css_selector('#text').clear()
                        browser.find_element_by_css_selector('#text').send_keys(texts[number])
                        browser.find_element_by_css_selector('#file').send_keys(audio_path)
                        time.sleep(2)
                        browser.find_element_by_css_selector('#eval').click()
                        time.sleep(2)
                        json_text=browser.find_element_by_css_selector('#result').text
                        json_text=re.sub(pattern,'',json_text)
    #                    print(json_text)
                        sheet_save.write(number, 2, json_text)  
            except:
                print(number)
                browser.quit()
                excel_save_copy.save(save_path) 
                break
        excel_save_copy.save(save_path) 
    browser.quit()
            