# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 10:23:07 2018

@author: bnuzgn
"""

import os
import re

filePath=r'C:\Users\bnuzgn\Desktop\LetsGO\Text'

list_1 =os.listdir(filePath)
for i in range(0,len(list_1)):
    print(list_1[i])