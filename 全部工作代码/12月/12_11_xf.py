# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 15:37:55 2018

@author: bnuzgn
"""

from xml.dom.minidom import parse
import xml.dom.minidom
import re

def parseXF(xf_str):
    pattern = re.compile(',(.*?)$',re.S)
    xf_str = pattern.findall(xf_str)[0]
    ret={}
    try:
        DOMTree = xml.dom.minidom.parseString(xf_str)
        xml_result = DOMTree.documentElement
        sentence_node=xml_result.getElementsByTagName('read_chapter')[0] 
        ret['xf_word_count']=float(sentence_node.getAttribute('word_count'))
        ret['xf_total_score']=float(sentence_node.getAttribute('total_score'))
        word_node_list = xml_result.getElementsByTagName('word')
        total_score=0
        xf_min_score=100
        for item in word_node_list:
            total_score+=float(item.getAttribute('total_score'))
            if xf_min_score>float(item.getAttribute('total_score')):
                xf_min_score=float(item.getAttribute('total_score'))
        if ret['xf_word_count']!=0:
            xf_ave_score = total_score/ret['xf_word_count']
        ret['xf_min_score']=xf_min_score
        ret['xf_ave_score']=xf_ave_score
        return ret
    except Exception as e:
        ret['xf_total_score']=0
        ret['xf_word_count']=0
        ret['xf_min_score']=0
        ret['xf_ave_score']=0
        print (e)
        return ret
        

if __name__=='__main__':
    xf_path=r'C:\Users\bnuzgn\Desktop\putao\12_11\123.txt'
    with open(xf_path)as f:
        xf_str=f.read()
#    print(xf_str)
    print(parseXF(xf_str))