# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 11:53:57 2019

@author: bnuzgn
该功能用于读取某个目录下所有的txt文件（默认是对话文件）并且生成一个
"""

import json
import os
import re
import sys

def Middleprocess(sentenceList,FirstSentenceDict,SecondtSentenceDict):
    '''处理ReadFile返回的sentenceList'''
    firstLine = sentenceList[0]
    secondLine = sentenceList[1]
    firstLineList = re.split(r"([.!?])", firstLine)
    firstLineList.append("")
    firstLineList = ["".join(i) for i in zip(firstLineList[0::2],firstLineList[1::2])]
    secondLineList = re.split(r"([.!?])", secondLine)
    secondLineList.append("")
    secondLineList = ["".join(i) for i in zip(secondLineList[0::2],secondLineList[1::2])]
    '''对句子进行去重'''
    firstLineList = list(set(firstLineList))
    secondLineList = list(set(secondLineList))
    '''对于firstLineList中的每一句进行判断并插入FirstSentenceDict中'''
    for sentence_1st in firstLineList:
        sentence_1st = sentence_1st.strip()
        if len(sentence_1st)>3:
            for sentence_2nd in secondLineList:
                sentence_2nd = sentence_2nd.strip()
                if len(sentence_2nd)>3:
                    '''将sentence_1st放入字典中并在其中保存sentence_2nd的信息'''
                    if sentence_1st in FirstSentenceDict:
                        if sentence_2nd in FirstSentenceDict[sentence_1st]:
                            FirstSentenceDict[sentence_1st][sentence_2nd]+=1
                        else:
                            FirstSentenceDict[sentence_1st][sentence_2nd]=1
                    else:
                        FirstSentenceDict[sentence_1st]={sentence_2nd:1}
    '''对于secondLineList中的每一句进行判断并插入SecondtSentenceDict中'''
    for sentence_2nd in secondLineList:
        sentence_2nd = sentence_2nd.strip()
        if len(sentence_2nd)>3:
            for sentence_1st in firstLineList:
                sentence_1st = sentence_1st.strip()
                if len(sentence_1st)>3:
                    '''将sentence_2nd放入字典中并在其中保存sentence_1st的信息'''
                    if sentence_2nd in SecondtSentenceDict:
                        if sentence_1st in SecondtSentenceDict[sentence_2nd]:
                            SecondtSentenceDict[sentence_2nd][sentence_1st]+=1
                        else:
                            SecondtSentenceDict[sentence_2nd][sentence_1st]=1
                    else:
                        SecondtSentenceDict[sentence_2nd]={sentence_1st:1}

def ReadFile(dirpath,filename,FirstSentenceDict,SecondtSentenceDict):
    with open(os.path.join(dirpath,filename),'r',encoding = 'utf-8') as f:
        firstLine = ''
        secondLine = ''
        while True:
            newline = f.readline().strip()
            sentenceList = []
            '''结束条件'''
            if newline is '':
                break
            ''''''
            if firstLine == '':
                firstLine = newline
                continue
            elif secondLine == '':
                secondLine = newline
                sentenceList.append(firstLine)
                sentenceList.append(secondLine)
                Middleprocess(sentenceList,FirstSentenceDict,SecondtSentenceDict)
            else:
                firstLine = secondLine
                secondLine = newline
                sentenceList.append(firstLine)
                sentenceList.append(secondLine)
                Middleprocess(sentenceList,FirstSentenceDict,SecondtSentenceDict)
            

def start():
    '''
      两种使用方法：
        1.在IDE中运行
        2.在命令行中使用
    '''
    if len(sys.argv)<2:
        '''IDE运行'''
#        file_dir_path = r'C:\Users\bnuzgn\Desktop\total'
        file_dir_path = r'C:\Users\bnuzgn\Desktop\total'
        MiddleFirstSentenceJson=r'C:\Users\bnuzgn\Desktop\MiddleFirstSentence.json'
        MiddleSecondtSentenceJson=r'C:\Users\bnuzgn\Desktop\MiddleSecondtSentence.json'
        FirstSentenceJson=r'C:\Users\bnuzgn\Desktop\FirstSentence.json'
        SecondtSentenceJson=r'C:\Users\bnuzgn\Desktop\SecondtSentence.json'
    elif len(sys.argv)==6:
        '''命令行运行'''
        file_dir_path = sys.argv[1]
        MiddleFirstSentenceJson = sys.argv[2]
        MiddleSecondtSentenceJson = sys.argv[3]
        FirstSentenceJson = sys.argv[4]
        SecondtSentenceJson = sys.argv[5]
    else:
        '''出现错误'''
        print('参数错误：参数1为读取路径,2为首句中间文件json位置，3为回答句中间文件json位置，4为首句中间文件json位置，5为回答句文件json位置')
        return
    if not os.path.isdir(file_dir_path):
        print('不存在'+file_dir_path)
        return
    '''打开json文件'''
    with open(MiddleFirstSentenceJson,'w+')as f: 
        if f.read():
            FirstSentenceDict = json.loads(f.read())
        else:
            FirstSentenceDict = {}
    with open(MiddleSecondtSentenceJson,'w+')as f:
        if f.read():
            SecondtSentenceDict = json.loads(f.read())
        else:
            SecondtSentenceDict = {}
    ''''''
    for dirpath,dirnames,filenames in os.walk(file_dir_path):
        for filename in filenames:
            if filename[-4:]== '.txt':
#                print(filename)
                ReadFile(dirpath,filename,FirstSentenceDict,SecondtSentenceDict)
    '''打开json文件并保存中间文件'''
    with open(MiddleFirstSentenceJson,'w+')as f: 
        f.write(json.dumps(FirstSentenceDict))
    with open(MiddleSecondtSentenceJson,'w+')as f:
        f.write(json.dumps(SecondtSentenceDict))
    """
    开始进行统计工作
    1. FirstSentenceDict与SecondtSentenceDict是存储中间文件的字典，包含了所有的信息
    2. NewFirstSentenceDict与NewSecondtSentenceDict是经过统计之后的字典
    """
    maxNumber = 5
    '''条件阈值'''
    threshold = 1
    
    with open(FirstSentenceJson,'w+')as f: 
        if f.read():
            NewFirstSentenceDict = json.loads(f.read())
        else:
            NewFirstSentenceDict = {}
    with open(SecondtSentenceJson,'w+')as f:
        if f.read():
            NewSecondtSentenceDict = json.loads(f.read())
        else:
            NewSecondtSentenceDict = {}
     
    '''开始处理FirstSentenceDict'''

    for item in FirstSentenceDict:
        '''当内部符合条件的数量不超过设置数量时，全部导入'''
        '''统计符合条件的数量'''
        thresholdNumber = 0
        for subItem in FirstSentenceDict[item]:
            if FirstSentenceDict[item][subItem] > threshold:
                thresholdNumber += 1
        """如果符合则全部导入"""
        if thresholdNumber <= maxNumber:
                for subItem in FirstSentenceDict[item]:
                    if FirstSentenceDict[item][subItem] > threshold:
                        if item not in NewFirstSentenceDict:
                            NewFirstSentenceDict[item] = {subItem:FirstSentenceDict[item][subItem]}
                        else:
                            NewFirstSentenceDict[item][subItem] = FirstSentenceDict[item][subItem]
        
        else:
            """如果不符合则执行排序功能"""
            count = 0
            while count < maxNumber:
                '''每次找到最大值并保存进NewFirstSentenceDict中'''
                maxKey = ''
                maxValue = threshold-1
                if item not in NewFirstSentenceDict:
                    NewFirstSentenceDict[item]={}
                for subItem in FirstSentenceDict[item]:
                    if FirstSentenceDict[item][subItem] > maxValue:
                        maxKey = subItem
                        maxValue = FirstSentenceDict[item][subItem]
                if maxKey not in NewFirstSentenceDict[item]:
                        NewFirstSentenceDict[item][maxKey] = FirstSentenceDict[item][maxKey]
                count += 1
    '''开始处理SecondtSentenceDict'''
    for item in SecondtSentenceDict:
        '''当内部符合条件的数量不超过设置数量时，全部导入'''
        '''统计符合条件的数量'''
        thresholdNumber = 0
        for subItem in SecondtSentenceDict[item]:
            if SecondtSentenceDict[item][subItem] > threshold:
                thresholdNumber += 1
        """如果符合则全部导入"""
        if thresholdNumber <= maxNumber:
                for subItem in SecondtSentenceDict[item]:
                    if SecondtSentenceDict[item][subItem] > threshold:
                        if item not in NewSecondtSentenceDict:
                            NewSecondtSentenceDict[item] = {subItem:SecondtSentenceDict[item][subItem]}
                        else:
                            NewSecondtSentenceDict[item][subItem] = SecondtSentenceDict[item][subItem]
        
        else:
            """如果不符合则执行排序功能"""
            count = 0
            while count < maxNumber:
                '''每次找到最大值并保存进NewFirstSentenceDict中'''
                maxKey = ''
                maxValue = threshold-1
                if item not in NewSecondtSentenceDict:
                    NewSecondtSentenceDict[item]={}
                for subItem in SecondtSentenceDict[item]:
                    if SecondtSentenceDict[item][subItem] > maxValue:
                        maxKey = subItem
                        maxValue = SecondtSentenceDict[item][subItem]
                if maxKey not in NewSecondtSentenceDict[item]:
                        NewSecondtSentenceDict[item][maxKey] = SecondtSentenceDict[item][maxKey]
                count += 1       
    '''打开json文件并保存结果文件'''
    with open(FirstSentenceJson,'w+')as f: 
        f.write(json.dumps(NewFirstSentenceDict))
    with open(SecondtSentenceJson,'w+')as f:
        f.write(json.dumps(NewSecondtSentenceDict))
        
if __name__=='__main__':
    start()