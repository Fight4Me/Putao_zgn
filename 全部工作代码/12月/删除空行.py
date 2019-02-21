# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 10:58:28 2018

@author: bnuzgn
"""
import os

file_dir_path = r'C:\Users\bnuzgn\Desktop\WebSpider\ForBeginners_\Text'
save_dir_path = r'C:\Users\bnuzgn\Desktop\WebSpider\ForBeginners_'

def createDir(save_dir_path):
    if os.path.isdir(save_dir_path):
        new_dir_path = os.path.join(save_dir_path,'New')
        if os.path.isdir(new_dir_path):
            print('已有文件夹'+new_dir_path)
            return new_dir_path
        else:
            os.mkdir(new_dir_path)
            print('成功创建文件夹'+new_dir_path)
            return new_dir_path

def delete(dirpath,filename,new_dir_path):
    with open (os.path.join(dirpath,filename),'r',encoding='utf-8')as f:
        new_txt = ''
        lines = f.readlines()
        for line in lines:
            line = line.lstrip()
            if line is not '':
                new_txt += line
    with open(os.path.join(new_dir_path,filename),'w')as f:
        f.write(new_txt)

if __name__=='__main__':
    new_dir_path = createDir(save_dir_path)
    for dirpath,dirnames,filenames in os.walk(file_dir_path):
        for filename in filenames:
            delete(dirpath,filename,new_dir_path)