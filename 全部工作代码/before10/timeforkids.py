# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 14:24:19 2018

@author: bnuzgn
"""
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

#browser = webdriver.PhantomJS()
browser = webdriver.Chrome()
browser.implicitly_wait(10)

homepage=r'https://www.timeforkids.com/g56/'

def download_page(url):
    detail_browser=webdriver.Chrome()
    detail_browser.implicitly_wait(10)
    try:
        detail_browser.get(url)    
        time.sleep(10)
    finally:
        detail_browser.quit()
        
        
if __name__=='__main__':
    url_unique=[]
    browser.get(homepage)
    wait=WebDriverWait(browser,400)
    while(True):
        time.sleep(1)
        wait=WebDriverWait(browser,400)
        button=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.BJXwjRnc')))
        try:
            button.click()
        except:
            break
    button=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.BJXwjRnc')))#目的是使得页面加载完毕
    url_list=browser.find_elements_by_css_selector('#app .column .row a')
    for i in url_list:
        url=i.get_attribute('href')
        if(re.search(r'https://www.timeforkids.com/g56/',str(url))and not re.search(r'https://www.timeforkids.com/g56/sections',str(url))):
#        print(url)
            if not (str(url) in url_unique):
                print(url)
                url_unique.append(url)
    browser.quit()