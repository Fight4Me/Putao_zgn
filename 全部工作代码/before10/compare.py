# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 11:18:14 2018

@author: bnuzgn
"""

import os
import re

file_path_1=r'C:\Users\bnuzgn\Desktop\WebSpider\Storynory_old\Audio'
file_path_2=r'C:\Users\bnuzgn\Desktop\WebSpider\Storynory_old\New'


def compare_audio_text(file_path_1,file_path_2):
    audio=[]
    text=[]
    list1 =os.listdir(file_path_1) 
    list2 =os.listdir(file_path_2) 
    for i in range(0,len(list1)):
        audio_name=re.sub('.mp3','',list1[i])
        audio.append(audio_name)
#        print(name)
        
    for j in range(0,len(list2)):
        text_name=re.sub('.txt','',list2[j])
#        print(name)
        text.append(text_name)
    for a in audio:
        if a not in text:
            print(file_path_2+" !!!do not have!!! "+a)
    for t in text:
        if t not in audio:
            print(file_path_1+" !!!do not have!!! "+t)
            
            
compare_audio_text(file_path_1,file_path_2)