# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 14:10:19 2018

@author: bnuzgn
"""

from selenium import webdriver 
import time
import os
import re

dic={
     "1":"Name",
     "2":"Kate",
     "3":"Andy",
     "4":"My name is Kate.",
     "5":"My name is Andy.",
     "6":"What’s your name?",
     "7":"ball",
     "8":"yo-yo",
     "9":"jump rope",
     "10":"bicycle",
     "11":"What is it?",
     "12":"It‘s a jump rope.",
     "13":"It’s a ball.",
     "14":"It’s a bicycle.",
     "15":"It’s a yo-yo.",
     "16":"Teddy bear",
     "17":"Car",
     "18":"Train",
     "19":"Doll",
     "20":"Is it a teddy bear?",
     "21":"Yes, it’s a teddy bear.",
     "22":"Is it a car?",
     "23":"Yes, it’s a car.",
     "24":"Is it a train?",
     "25":"Yes, it’s a train.",
     "26":"Is it a doll?",
     "27":"Yes, it’s a doll.",
     "28":"Throw a ball",
     "29":"Catch a ball",
     "30":"Bounce a ball",
     "31":"What can you do?",
     "32":"I can throw a ball.",
     "33":"I can catch a ball.",
     "34":"I can bounce a ball.",
     "35":"Ride a bicycle",
     "36":"Play a ball",
     "37":"Let’s  ride a bicycle?",
     "38":"Let’s play a ball.",
     "39":"Let’s jump rope.",
     }

browser = webdriver.Chrome()

audio_2=['1','2','3','7','8','10','17','18','19']
homepage=r'https://demo.chivox.com/hl/all_in_one/'
file_path_2=r'C:\Users\bnuzgn\Desktop\rec_ch'

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
    browser.get(homepage)
    time.sleep(10)
    list2 =os.listdir(file_path_2) 
    for i in list2:
        if(re.search(r'.mp3$',i)):
            number=re.sub(r'.mp3','',i)
            browser.find_element_by_css_selector('input[value=sentence]').click()
            browser.find_element_by_css_selector('.text').clear()
            browser.find_element_by_css_selector('.text').send_keys(dic[number])
            audio_path=os.path.join(file_path_2,i)
            browser.find_element_by_css_selector('#file_audioFile').send_keys(os.path.join(file_path_2,i))
            time.sleep(3)
            browser.find_element_by_css_selector('#btn_sunmmit').click()
            time.sleep(5)
            json_text=browser.find_element_by_css_selector('.jsonrst').text
#            print(json_text)
            with open(os.path.join(file_path_2,number)+'.cs.txt','a') as f:
                f.write(json_text)    
                print(number)
            time.sleep(1)
    browser.quit()