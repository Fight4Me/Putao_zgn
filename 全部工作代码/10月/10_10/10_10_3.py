# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 16:15:42 2018

@author: bnuzgn
"""

import os 
import re
import json
import time
from pydub import AudioSegment

def trans_wav_to_mp3(wav_path,mp3_path):
    song = AudioSegment.from_wav(wav_path)
    song.export(mp3_path, format="mp3")

read_path = r'C:\Users\bnuzgn\Desktop\10_10\operate.txt'
check_path = r'C:\Users\bnuzgn\Desktop\10_10\hyf_data_res\sentence'

if __name__ == '__main__' :
    try:
        with open(read_path,encoding='utf-8')as f:
            read_lines=f.readlines()
            for line in read_lines:
                list1=line.strip().split('\t')
                each_folder_path = os.path.join(check_path,list1[9],list1[10])
                list2 =os.listdir(each_folder_path)
    #            print(list2)
    #            time.sleep(2)
                for file_name in list2:
                    if(re.search('^[^\.].*\.wav$',file_name)):
                        wav_path = os.path.join(each_folder_path,file_name)
                        mp3_path = os.path.join(each_folder_path,re.sub(r'.wav$','',file_name)+r'.mp3')
    #                    print(mp3_path)
                        trans_wav_to_mp3(wav_path,mp3_path)
    except Exception as e:
        print(file_name)
        print(mp3_path)
        print(e)
            