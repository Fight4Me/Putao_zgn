# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 12:11:55 2018

@author: bnuzgn
"""
import json

def parseYZS(yzs_str):
    ret={}
    if yzs_str=='':
        ret['yzs_Is_ok']=0
        ret['yzs_score']=0
        ret['yzs_fluency']=0
        ret['yzs_pronunciation']=0
        ret['yzs_integrity']=0
        ret['yzs_Type_0_num']=0
        ret['yzs_Type_1_num']=0
        ret['yzs_Word_num']=0
        ret['yzs_Min_score']=0
        ret['yzs_Avg_score']=0
        return ret
    else:
        yzs_json = json.loads(yzs_str)
        if yzs_json['EvalType']!='general':
            ret['yzs_Is_ok']=0
            ret['yzs_score']=0
            ret['yzs_fluency']=0
            ret['yzs_pronunciation']=0
            ret['yzs_integrity']=0
            ret['yzs_Type_0_num']=0
            ret['yzs_Type_1_num']=0
            ret['yzs_Word_num']=0
            ret['yzs_Min_score']=0
            ret['yzs_Avg_score']=0
            return ret
        else:
            ret['yzs_Is_ok']=1
            ret['yzs_score']=yzs_json['score']
            ret['yzs_fluency']=yzs_json['lines'][0]['fluency']
            ret['yzs_pronunciation']=yzs_json['lines'][0]['pronunciation']
            ret['yzs_integrity']=yzs_json['lines'][0]['integrity']
            ret['yzs_Word_num']=len(yzs_json['lines'][0]['words'])
            yzs_Type_0_num=0
            yzs_Type_1_num=0
            yzs_Min_score=100
            Total_score=0
            for items in yzs_json['lines'][0]['words']:
                if items['type']==0:
                    yzs_Type_0_num+=1
                if items['type']==1:
                    yzs_Type_1_num+=1
                if yzs_Min_score > items['score']:
                    yzs_Min_score = items['score']
                Total_score+=items['score']
            ret['yzs_Type_0_num']=yzs_Type_0_num
            ret['yzs_Type_1_num']=yzs_Type_1_num
            ret['yzs_Min_score']=yzs_Min_score
            if ret['yzs_Word_num']-yzs_Type_0_num-yzs_Type_1_num !=0:
                ret['yzs_Avg_score']=Total_score/ret['yzs_Word_num']-yzs_Type_0_num-yzs_Type_1_num
            else:
                ret['yzs_Avg_score']=0
            return ret

def parseXS(xs_str):
    ret={}
    if xs_str=='':
        ret['xs_Is_ok']=0
        ret['xs_accuracy']=0
        ret['xs_integrity']=0
        ret['xs_overall']=0
        ret['xs_Word_num']=0
        ret['xs_Min_score']=0
        ret['xs_Avg_score']=0
        return ret
    else:
        xs_json=json.loads(xs_str)
        if xs_json['result']['overall']==0:
            ret['xs_Is_ok']=0
            ret['xs_accuracy']=0
            ret['xs_integrity']=0
            ret['xs_overall']=0
            ret['xs_Word_num']=0
            ret['xs_Min_score']=0
            ret['xs_Avg_score']=0
            return ret
        else:
            ret['xs_Is_ok']=1
            ret['xs_accuracy']=xs_json['result']['accuracy']
            ret['xs_integrity']=xs_json['result']['integrity']
            ret['xs_overall']=xs_json['result']['overall']
            ret['xs_Word_num']=len(xs_json['result']['details'])
            xs_Min_score=100
            Total_score=0
            for xs_item in xs_json['result']['details']:
                if xs_Min_score>xs_item['score']:
                    xs_Min_score=xs_item['score']
                Total_score+=xs_item['score']
            if ret['xs_Word_num']==0:
                ret['xs_Avg_score']=Total_score/ret['xs_Word_num']
            else:
                ret['xs_Avg_score']=0
            ret['xs_Min_score']=xs_Min_score
            return ret

def parseSG(sg_str):
    ret={}
    if sg_str=='':
        ret['sg_Is_ok']=0
        ret['sg_accuracy']=0
        ret['sg_fluency']=0
        ret['sg_integrity']=0
        ret['sg_overall']=0
        ret['sg_Word_num']=0
        ret['sg_Min_score']=0
        ret['sg_Avg_score']=0
        ret['sg_Del_num']=0
        ret['sg_Ins_num']=0
        return ret
    else:
        sg_json=json.loads(sg_str)
        if sg_json['result']['overall']=="0":
            ret['sg_Is_ok']=0
            ret['sg_accuracy']=0
            ret['sg_fluency']=0
            ret['sg_integrity']=0
            ret['sg_overall']=0
            ret['sg_Word_num']=0
            ret['sg_Min_score']=0
            ret['sg_Avg_score']=0
            ret['sg_Del_num']=0
            ret['sg_Ins_num']=0
            return ret
        else:
            ret['sg_Is_ok']=1
            ret['sg_accuracy']=float(sg_json['result']['accuracy'])
            ret['sg_fluency']=float(sg_json['result']['fluency'])
            ret['sg_integrity']=float(sg_json['result']['integrity'])
            ret['sg_overall']=float(sg_json['result']['overall'])
            ret['sg_Word_num']=len(sg_json['result']['word'])
            '''
                遍历字典获取分数等信息
            '''
            sg_Min_score=100
            Total_score=0
            sg_Del_num=0
            sg_Ins_num=0
            for dic_item in sg_json['result']['word']:
                #print(dic_item)
                if dic_item['type']=='delete':
                    sg_Del_num+=1
                    continue
                if dic_item['type']=='insert':
                    sg_Ins_num+=1
                    continue
                if sg_Min_score > float(dic_item['score']):
                    sg_Min_score = float(dic_item['score'])
                Total_score += float(dic_item['score'])
            if ret['sg_Word_num']-sg_Del_num-sg_Ins_num!=0:
                sg_Avg_score = Total_score/(ret['sg_Word_num']-sg_Del_num-sg_Ins_num)
            else:
                sg_Avg_score = 0
            ret['sg_Min_score']=sg_Min_score
            ret['sg_Avg_score']=sg_Avg_score
            ret['sg_Del_num']=sg_Del_num
            ret['sg_Ins_num']=sg_Ins_num
            return ret
        
if __name__=='__main__':
    sg_path=r'C:\Users\bnuzgn\Desktop\putao\12_11\sg.json'
    xs_path=r'C:\Users\bnuzgn\Desktop\putao\12_11\xs.json'
    yzs_path=r'C:\Users\bnuzgn\Desktop\putao\12_11\yzs.json'
    with open(sg_path)as f:
        sg_str=f.read()
    with open(xs_path)as f:
        xs_str=f.read()
    with open(yzs_path)as f:
        yzs_str=f.read()
#    print(parseSG(sg_str))
#    print(parseXS(xs_str))
    print(parseYZS(yzs_str))