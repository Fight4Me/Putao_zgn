# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 15:08:10 2018

@author: bnuzgn
"""
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import os

#browser = webdriver.PhantomJS()

total_path=r'C:\Users\bnuzgn\Desktop\url.txt'
compare_path=r'C:\Users\bnuzgn\Desktop\url_already.txt'
file_path=r'C:\Users\bnuzgn\Desktop\WebSpider\timeforkids\Text'

detail_browser=webdriver.Chrome()

def download_page(url):
    time.sleep(2)
    try:
        detail_browser.get(url)    
        wait=WebDriverWait(detail_browser,30)
        texts=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'p')))
        time.sleep(8)
        texts=detail_browser.find_elements_by_css_selector('p')
        text=''
        name=re.sub(r'https://www.timeforkids.com/g56/','',url)
        name=re.sub(r'/','',name)
        for i in texts:
            text=text+i.text+'\n'
        download_path=os.path.join(file_path,name)
        download_path=download_path+'.txt'
        with open(download_path,'w',encoding='utf-8') as f:
            f.write(text)
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        pass
        
        
if __name__=='__main__':
    total=[]
    compare=[]
    with open(total_path,'r',encoding='utf-8') as f:
        readline=f.readlines()
        for line in readline:
            line=re.sub(r'\n','',line)
            total.append(line)
    with open(compare_path,'r',encoding='utf-8') as f:
        readline=f.readlines()
        for line in readline:
            line=re.sub(r'\n','',line)
            compare.append(line)
    for url in total:
#        print(url)
        if(url not in compare):
            print(url)
            if (download_page(url)):
                compare.append(url)                    
            else:
                break
    used_url=''
    for i in compare:
        used_url=used_url+i+'\n'
    with open(compare_path,'w',encoding='utf-8') as f:
        f.write(used_url)
    detail_browser.quit()