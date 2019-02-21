# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 15:05:46 2019

@author: bnuzgn
"""

def count(line):
    layer = 0
    while True:
        if line[:4]=='----':
            layer+=1
            line = line[4:]
        else:
            break
    return layer
        
    
def reads(line,lastNumber,lastLayer):
    layer = count(line)
    if layer==lastLayer:
        number = lastNumber+1
    elif layer>lastLayer:
        diff = layer-lastLayer
        number = lastNumber*(10**diff)+1
    else:
        diff = lastLayer-layer
        number = lastNumber//(10**diff)+1
    return number,layer

if __name__=='__main__':
    file_path = r'C:\Users\bnuzgn\Desktop\L1-1-1-1.txt'
    save_path = r'C:\Users\bnuzgn\Desktop\NewLL1-1-1-1.txt'
    number = 0
    layer = 0
    str1 = ''
    with open(file_path,'r',encoding='utf-8')as f:
        lines = f.readlines()
    for line in lines:
        number,layer = reads(line,number,layer)
        str1 +=str(number)+'\t'+line
    with open(save_path,'w',encoding='utf-8')as f:
        f.write(str1)