# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 14:43:49 2019

@author: bnuzgn
"""

import json
from word2pron import sent2phoneSeq 

sent = 'jump rope'

if __name__=='__main__':
    wordList = sent.split()
    yinsuList = []
    yinbiaoList = []
    for word in wordList:
        yinsuList.append(sent2phoneSeq(word,1))
        yinbiaoList.append(sent2phoneSeq(word,2))
    wordNum = len(wordList)
    sentDic = {}
    sentDic['words']=[]
    sentDic['sentence']='0'
    for i in range(wordNum):
        tmpList = []
        tmpDic ={wordList[i]:tmpList}
        sentDic['words'].append(tmpDic)
        
        yinsuTypeNum = len(yinsuList[i])
        for j in range(yinsuTypeNum):
            tmpList2 = []

            yinsuNum = len(yinbiaoList[i][j])
            tmpList2.append(yinbiaoList[i][j])
            tmpList2.append(yinsuList[i][j])
            tmpList2.append(['1']*yinsuNum)
            tmpList2.append(['0']*yinsuNum)
            tmpDic2 = {'pron'+str(j+1):tmpList2}
            sentDic['words'][i][wordList[i]].append(tmpDic2)
         sentDic['words'][i][wordList[i]].append({'label':'0','pron':'1'})
            
    print json.dumps(sentDic)