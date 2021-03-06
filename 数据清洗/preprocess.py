# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 17:25:18 2018

@author: bnuzgn
"""
"""
注意：使用该服务需要启动斯坦福NER：使用7-class模型，请预先启动服务并修改端口号
Windows用户：
1.打开Git Bash
2. bash ner.sh
"""

import sys
import re
import os
import ner

table = {ord(f):ord(t) for f,t in zip(
     u'…，。！？【】（）％＃＠＆１２３４５６７８９０’—',
     u'.,.!?[]()%#@&1234567890\'-')}

def createDir(save_dir_path): 
    '''用于判断并新建save文件夹'''
    if os.path.isdir(save_dir_path):
        return save_dir_path
    else:
        os.mkdir(save_dir_path)
        return save_dir_path

def NameDicReplace(line,nameDicList):
    '''词典'''
    for name in nameDicList:
        if ' '+name+' ' in line:
            line = line.replace(name,'<PERSON>')        
    return line
        

def NerReplace(line,tagger):
    '''斯坦福NER'''
    index_list = ['LOCATION','PERSON','ORGANIZATION','MONEY','PERCENT','DATE','TIME']
    ner_dic=tagger.get_entities(line)
    if ner_dic:
        for index in index_list:
            if index in ner_dic:
                for item in ner_dic[index]:
                    line = line.replace(item,'<'+index+'>')
    return line
        

def RowProcess(dirpath,filename,new_dir_path):
    '''行处理'''
    name_list=[]
    pattern_1 = re.compile('^.*?:.*$')
    pattern_2 = re.compile('(.*?):.*')
    pattern_3 = re.compile('^.*?:(.*?)$')
    try:
        with open (os.path.join(dirpath,filename),'r',encoding = 'utf-8')as f:
            names = ''
            new_text = ''
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                '''中文字符处理与全半角转换'''
        #                line = unicodedata.normalize('NFKC', line)
                line = line.translate(table)
                
                if line is not '' and re.match(pattern_1,line):  
                    '''保存姓名信息'''
                    name = re.findall(pattern_2,line)[0]
                    if name not in name_list:
                        name_list.append(name.strip())
                    '''保存对话部分'''
                    diaLine = re.findall(pattern_3,line)[0].strip()
                    new_text += diaLine+'\n'
        name_path = os.path.join(new_dir_path,filename[:-4]+'.list')
        new_text = new_text.strip()
        if new_text:
            for name in name_list:
                names+=name+'\n'
            with open(name_path,'w',encoding = 'utf-8')as f:
                '''保存'''
                f.write(names)
            with open(os.path.join(new_dir_path,filename),'w',encoding = 'utf-8')as f:
                '''保存'''
                f.write(new_text)
        else:
            print(os.path.join(dirpath,filename)+'没有对话内容')
        #            os.remove(os.path.join(new_dir_path,filename))
        #            os.remove(os.path.join(new_dir_path,filename[:-4]+'.list'))
            return None
        return name_list
    except Exception as e:
        print('RowProcess Error：'+os.path.join(dirpath,filename))
        print(e)
        print('try again!')
        try:
            with open (os.path.join(dirpath,filename),'r')as f:
                names = ''
                new_text = ''
                lines = f.readlines()
                for line in lines:
                    line = line.strip()
                    '''中文字符处理与全半角转换'''
            #                line = unicodedata.normalize('NFKC', line)
                    line = line.translate(table)
                    
                    if line is not '' and re.match(pattern_1,line):  
                        '''保存姓名信息'''
                        name = re.findall(pattern_2,line)[0]
                        if name not in name_list:
                            name_list.append(name.strip())
                        '''保存对话部分'''
                        diaLine = re.findall(pattern_3,line)[0].strip()
                        new_text += diaLine+'\n'
            name_path = os.path.join(new_dir_path,filename[:-4]+'.list')
            new_text = new_text.strip()
            if new_text:
                for name in name_list:
                    names+=name+'\n'
                with open(name_path,'w',encoding = 'utf-8')as f:
                    '''保存'''
                    f.write(names)
                with open(os.path.join(new_dir_path,filename),'w',encoding = 'utf-8')as f:
                    '''保存'''
                    f.write(new_text)
            else:
                print(os.path.join(dirpath,filename)+'没有对话内容')
            #            os.remove(os.path.join(new_dir_path,filename))
            #            os.remove(os.path.join(new_dir_path,filename[:-4]+'.list'))
                return None
            print('try again!成功')
            return name_list
        except Exception as e:
            print('RowProcess Error：'+os.path.join(dirpath,filename))
            print(e)
        
        
def WordProcess(dirpath,filename,new_dir_path,name_list,nameDicList,tagger):
    '''单词处理'''
    pattern_1=re.compile('[A-Za-z]+\d+[\.\?,!]*')
    pattern_2=re.compile('(.*?)\d+')
    '''存储不能作为姓名的信息'''
    pattern_3=re.compile('[a-zA-Z]')
    try:
        with open (os.path.join(new_dir_path,filename),'r',encoding='utf-8')as f:
            new_txt = ''
            lines = f.readlines()
        '''存储姓名信息'''
        nameList = []
        with open(os.path.join(new_dir_path,filename[:-4]+'.list'),encoding = 'utf-8')as f:
            nameLines = f.readlines()
        for nameLine in nameLines:
            nameList.append(nameLine.strip())
#        print(nameList)
        for line in lines:
            line = line.lstrip()
            if line is not '':
                '''将常见标点符号与单词分开'''
                line = line.replace(',',' , ').replace('.',' . ').replace('?',' ? ').replace('!',' ! ').replace(':',' : ')
                '''将本文中出现的人名进行替换'''
                for name in nameList:
                    if not re.match(pattern_3,name):
                        if name in line:
                            line = line.replace(name,'<PERSON>')      
                '''姓名词典替换'''
                line = NameDicReplace(line,nameDicList)
                '''斯坦福ner替换'''
                line = NerReplace(line,tagger)
                
                words = line.split()
                for word in words:
                    '''用于对单词进行正则化'''
                    if re.match(pattern_1,word):
                        
                        '''去除单词末尾角标的情况'''
                        word = re.findall(pattern_2,word)[0]
                    word = word+' '
                    new_txt += word
                new_txt += '\n'     
        with open(os.path.join(new_dir_path,filename),'w',encoding = 'utf-8')as f:
            f.write(new_txt)
    except Exception as e:
        print('WordProcess Error：'+os.path.join(new_dir_path,filename))
        print(e)
        pass
        

def start():
    '''
      两种使用方法：
        1.在IDE中运行
        2.在命令行中使用
    '''
    if len(sys.argv)<2:
        '''IDE运行'''
        file_dir_path = r'C:\Users\bnuzgn\Desktop\SpeakingIsEasy'
        save_dir_path = r'C:\Users\bnuzgn\Desktop\SpeakingIsEasy2'
    elif len(sys.argv)==3:
        '''命令行运行'''
        file_dir_path = sys.argv[1]
        save_dir_path = sys.argv[2]
    else:
        '''出现错误'''
        print('参数错误：参数1为读取路径，2为保存路径。')
        return
    '''用于判断并新建save文件夹'''
    new_dir_path = createDir(save_dir_path)
    if not os.path.isdir(file_dir_path):
        print('不存在'+file_dir_path)
        return
    '''启动pynersocket'''
    tagger = ner.SocketNER(host='localhost', port=9191)
    '''读取name.list并加载'''
    nameDicPath = r'C:\Users\bnuzgn\Desktop\name.txt'
    with open(nameDicPath,'r',encoding='utf-8') as f:
        nameLines=f.readlines()
    nameDicList=[]
    for line in nameLines:
        nameDicList.append(line.split()[1])
    '''对file_dir_path文件中的所有文件进行处理'''
    for dirpath,dirnames,filenames in os.walk(file_dir_path):
        for filename in filenames:
            if filename[-4:] == '.txt':
                '''行处理'''
                name_list = RowProcess(dirpath,filename,new_dir_path)
                if not name_list:
                    continue
                '''单词处理'''
                WordProcess(dirpath,filename,new_dir_path,name_list,nameDicList,tagger)

if __name__=='__main__':
    start()