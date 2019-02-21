# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 12:45:46 2018

@author: bnuzgn
1. 该代码是日报代码的微缩版，用于发送salaryReport.py生成的excel文件。

"""
from __future__ import unicode_literals
import yagmail
import datetime
import pymysql
from sshtunnel import SSHTunnelForwarder
import re
from pyecharts import Line
import sys

def send_email(argv1):
	#链接邮箱服务器
	yag = yagmail.SMTP(user="zhangguannan@putao.com", password="Zmy64q2q83", host='smtp.putao.com')	
	
#	 发送邮件
	now_time = datetime.datetime.now().strftime('%Y%m%d')
	if argv1 == '1':
		yag.send(['bnuzgn@qq.com','zhangguannan@putao.com'],'['+now_time+']工资月报',contents = ['./salaryData/'+now_time+'.xls'])
	elif argv1 == '2':
		yag.send(['621038800@qq.com','zhangjunbo@putao.com','bnuzgn@qq.com','122502325@qq.com','heyu@putao.com','tongzijian@putao.com','621038800@qq.com'],'['+now_time+']工资月报',contents = ['./salaryData/'+now_time+'.xls'])
	

if __name__ == '__main__':
	argv1 = sys.argv[1]
	send_email(argv1)
