# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 11:37:17 2018

@author: bnuzgn
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import re
import os
import time

base_url = r'http://www.tingroom.com/lesson/xgnyyqsb1/list_4.html'
save_path = r'C:\Users\bnuzgn\Desktop\WebSpider\XinGaiNianYouth'

def save(title,text):
    file_path = os.path.join(save_path,title+'.txt')
    with open(file_path , 'w', encoding = 'utf-8')as f:
        f.write(text)

def craw(new_url):
    browser.execute_script('window.open("'+new_url+'");')
    handles = browser.window_handles
    browser.switch_to_window(handles[-1]) #切换到最新打开的窗口
#    browser.get(new_url)
    title = browser.find_element_by_css_selector('.title_viewbox h2').text
    title = title.strip().split()[1]
    items = browser.find_elements_by_css_selector('#zoom div')
    print(title)
    dia_text = ''
    for item in items:
        dia_text += item.text
        dia_text += '\n'
    save(title,dia_text)
    browser.close()
    browser.switch_to_window(handles[0])
    
    

def getIndex(base_url):
    li_list = browser.find_elements_by_css_selector('.listbox li')
    for item in li_list:
        new_url =item.find_element_by_tag_name('a').get_attribute('href')
#        print(new_url)
        craw(new_url)
    
if __name__ == '__main__':
    browser = webdriver.Chrome() 
    browser.get(base_url)
    getIndex(base_url)
    browser.quit()