# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 14:24:19 2018

@author: bnuzgn
"""
from selenium import webdriver 
import re
import os

#browser = webdriver.PhantomJS()
browser = webdriver.Chrome()
detail_browser=webdriver.Chrome()
browser.set_page_load_timeout(5)
detail_browser.set_page_load_timeout(10)
homepage=r'https://www.storiestogrowby.org/short-english-stories-kids-free/page/2/'
out_path=r'C:\Users\bnuzgn\Desktop\WebSpider\storiestogrowby\Text'

def download_page(url):
    try:
        detail_browser.get(url)   
    except Exception as e:
        detail_browser.execute_script('window.stop()')
        title=re.sub(r'https://www.storiestogrowby.org/story/','',url)
        title=re.sub(r'/','',title)
#        print(title)
        texts=detail_browser.find_elements_by_css_selector('.siteorigin-widget-tinymce span')
        txt=''
        for file_text in texts:
            txt=txt+file_text.text
#            print(file_text.text)
        file_path=os.path.join(out_path,title)+'.txt'
        with open(file_path,'w',encoding='utf-8') as f:
            f.write(txt)
    finally:
        pass
        
        
if __name__=='__main__':
    try:
        browser.get(homepage)
    except :
        browser.execute_script('window.stop()')
        url_list=browser.find_elements_by_css_selector('#vantage-grid-loop article .grid-thumbnail')
        for i in url_list:
            url=i.get_attribute('href')
            download_page(url)
    browser.quit()
    detail_browser.quit()