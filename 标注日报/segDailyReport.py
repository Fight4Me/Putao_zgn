# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 12:45:46 2018

@author: bnuzgn
"""
from __future__ import unicode_literals
import yagmail
import datetime
import pymysql
from sshtunnel import SSHTunnelForwarder
import re
from pyecharts import Line
import sys
import time

def send_email(argv1,today_task_number,today_review_number,total_task_number,total_review_number,total_number):
	#链接邮箱服务器
	yag = yagmail.SMTP(user="zhangguannan@putao.com", password="Zmy64q2q83", host='smtp.putao.com')	
	
	html = '<html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /></head><body>'	
	html += '<h3>切分标注情况</h3>'
	html += '当日切分标注完成数量：'+today_task_number+'<br>'
	html += '已完成切分标注总量：'+total_task_number+'<br>'
	html += '待标注总量：'+str(int(total_number)-int(total_task_number))+'<br>'
	html += '<h3>审核情况</h3>'
	html += '当日审核完成数量：'+today_review_number+'<br>'
	html += '已审核总量：'+total_review_number+'<br>'
	html += '待审核总量：'+str(int(total_task_number)-int(total_review_number))+'<br>'
	html +="""	
	</body>
	</html>
			"""
	
#	 发送邮件
	now_time = datetime.datetime.now().strftime('%Y%m%d')
	if argv1 == '1':
		yag.send(['bnuzgn@qq.com'],'['+now_time+']切分标注系统日报',contents = [html])
	elif argv1 == '2':
		yag.send(['621038800@qq.com','renli@putao.com','zhangjunbo@putao.com','heyu@putao.com'],'['+now_time+']切分标注系统日报',contents = [html])
	
	
sql1 = 'select distinct count(*) from Tagging_event where event_type=7 and TO_DAYS(Now())=TO_DAYS(event_date)' #今日标注数量
sql2 = 'select distinct count(*) from Tagging_event where event_type=62 and TO_DAYS(Now())=TO_DAYS(event_date)' #今日审核数量
sql3 = 'select count(*) from Tagging_task where task_type=10 and tagging_rate_1=1' #标注总数
sql4 = 'select count(*) from Tagging_task where task_type=10 and is_ok=1' #审核总数
sql5 = 'select count(*) from Tagging_task where task_type=10'

sql = [sql1,sql2,sql3,sql4,sql5]

pattern1 = re.compile('\((.*?),\)')

if __name__ == '__main__':
	argv1 = sys.argv[1]
	try:
		db = pymysql.connect(host = "127.0.0.1",port = 3306,user = "root",passwd = "tagging",database = "TaggingSys" ) 
	except:
		time.sleep(10)
		db = pymysql.connect(host = "127.0.0.1",port = 3306,user = "root",passwd = "tagging",database = "TaggingSys" ) 
	# 使用 cursor() 方法创建一个游标对象 cursors
	cursor = db.cursor()
	for i in range(0,len(sql)):
		cursor.execute(sql[i]) 
		if i is 0:
			ret = list(cursor.fetchall())
			if len(ret):
				for i in ret:
					today_task_number = pattern1.findall(str(i))[0]
			else:
				pass
			
		if i is 1:
			ret = list(cursor.fetchall())
			if len(ret):
				for i in ret:
					today_review_number = pattern1.findall(str(i))[0]
			else:
				pass
			
		if i is 2:
			ret = list(cursor.fetchall())
			if len(ret):
				for i in ret:
					total_task_number = pattern1.findall(str(i))[0]
			else:
				pass
		if i is 3:
			ret = list(cursor.fetchall())
			if len(ret):
				for i in ret:
					total_review_number = pattern1.findall(str(i))[0]
			else:
				pass
		if i is 4:
			ret = list(cursor.fetchall())
			if len(ret):
				for i in ret:
					total_number = pattern1.findall(str(i))[0]
			else:
				pass
		
#		print(str13)
	# 关闭数据库连接
	db.close()

	send_email(argv1,today_task_number,today_review_number,total_task_number,total_review_number,total_number)
