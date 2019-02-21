# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 14:10:19 2018

@author: bnuzgn
"""

from selenium.webdriver.common.keys import Keys
from selenium import webdriver 
import time

browser = webdriver.Chrome()
browser.implicitly_wait(10)

homepage=r'http://www.putaoedu.net.cn:8000/tagging/'

def process_page(url):
    browser.get(url)    
    lists=browser.find_elements_by_css_selector('.btn-danger')
    for lable in lists:
        lable.click()
    sub_button=browser.find_element_by_id('subbtn')
    sub_button.click()
    time.sleep(1)
    

if __name__=='__main__':
    browser.get(homepage)
    elem_user = browser.find_element_by_name("username")
    elem_user.send_keys("zgn")
    elem_pwd = browser.find_element_by_name("password")
    elem_pwd.send_keys("262012")
    elem_pwd.send_keys(Keys.RETURN)    
    browser.get('http://www.putaoedu.net.cn:8000/tagging/test/')
    url_detail=browser.find_element_by_css_selector('.container a').get_attribute('href')
    browser.execute_script('window.open()')
    browser.switch_to_window(browser.window_handles[1])
    process_page(url_detail)