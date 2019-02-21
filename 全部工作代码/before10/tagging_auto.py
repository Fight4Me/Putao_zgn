# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 14:10:19 2018

@author: bnuzgn
"""

from selenium.webdriver.common.keys import Keys
from selenium import webdriver 
import time
import re

browser = webdriver.Chrome()
browser.implicitly_wait(10)

homepage=r'http://193.112.75.135:8000/'

def process_page(url):
    browser.get(url)    
    lists=browser.find_elements_by_css_selector('.btn-group .btn-success')
    for lable in lists:
        lable.click()
    for i in range(2,101):
        next_button=browser.find_element_by_id('dataTable_next')
        next_button.click()
        lists=browser.find_elements_by_css_selector('.btn-group .btn-success')
        for lable in lists:
            lable.click()
    time.sleep(1)
    

if __name__=='__main__':
#    url_unique=[]
    browser.get(homepage)
    elem_user = browser.find_element_by_name("username")
    elem_user.send_keys("zgn")
    elem_pwd = browser.find_element_by_name("password")
    elem_pwd.send_keys("262012")
    elem_pwd.send_keys(Keys.RETURN)
#    browser.current_window_handle
#    browser.switch_to_alert()
#    time.sleep(1)
#    browser.accept()
#    print(browser.page_source())
    
    browser.get('http://193.112.75.135:8000/tagging/test/')
    url_detail=browser.find_element_by_css_selector('.container a').get_attribute('href')
#    print(url_detail)
    browser.execute_script('window.open()')
    browser.switch_to_window(browser.window_handles[1])
    process_page(url_detail)
    browser.quit()