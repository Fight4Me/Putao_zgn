# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 17:25:12 2018

@author: bnuzgn
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import re
import os
import time

browser = webdriver.PhantomJS()
browser_detail = webdriver.PhantomJS()
browser.implicitly_wait(10)
browser_detail.implicitly_wait(10)

filepath=r'C:\Users\bnuzgn\Desktop\WebSpider\kidsworldfun\Text'
url='https://www.kidsworldfun.com/shortstories_pt3.php'
        
def download_page(page_url):
    time.sleep(1)
    try:
        
        browser_detail.get(page_url)
        title=browser_detail.find_element_by_css_selector('.content_right h1:not(a)').text
        title=re.sub('Short Stories » ','',title)
        title=re.sub('\s+','_',title)
        contents=browser_detail.find_elements_by_css_selector('.con_welcome_sub3 p')
        content=''
        save_path=os.path.join(filepath,title)
        save_path=save_path+'.txt'
        print(save_path)
        for content_line in contents:
#            print(content.text)
            content=content+'\n'+content_line.text
        with open(save_path,'w',encoding='utf-8')as f:
            f.write(content)
    except Exception as e:
        print(e)
        
    
#download_page(url)
if __name__ == '__main__': 
    browser.get(url)
    contents=browser.find_elements_by_css_selector('.poem_list li a')
    for content in contents:
#        print('ok')
        page_url=content.get_attribute('href')
#        print(page_url)
        download_page(page_url)
    browser.close()
        