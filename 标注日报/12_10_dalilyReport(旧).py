# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 12:45:46 2018

@author: bnuzgn

1. send_email函数接收主函数的参数生成html并且发送日报。
2. echarts_plot函数用于绘图
3. 主函数用于连接数据库进行查询工作。

代码使用时需要使用python3
代码接收参数1和2，1用于向自己传递邮件，2用于实际生产功能，具体使用方式请参考tagging虚拟机中crontab的配置
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

def send_email(argv1,today_task_number,total_finished_task_number,proportion,today_active_number,total_tagging_people,str5,str6,today_verified_task_number,verified_proportion,str9,html_path,html2_path,str12,str13,str16,unReviewed_number,total_verified_task_number):
	#链接邮箱服务器
	yag = yagmail.SMTP(user="zhangguannan@putao.com", password="Zmy64q2q83", host='smtp.putao.com')	
	
	html = '<html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /></head><body>'	
	html += '<h3>标注情况</h3>'
	html += '当日标注完成数量：'+today_task_number+'<br>'
	html += '已完成标注量：'+total_finished_task_number+'<br>'
	html += '标注进度：'+proportion+'<br>'
	html += '今日活跃人数：'+today_active_number +'<br>'
	html += '总标注人数：'+total_tagging_people+'<br>'
	html += '<a href =\'http://60.195.40.162:8000/tagging/report/\'>点我看近十日标注量变化曲线</a><br>'
	html += '<h3>审核情况</h3>'
	html += '当日审核完成数量：'+today_verified_task_number+'<br>'
	html += '审核进度：'+verified_proportion+'<br>'
	html += '已审核数量：'+total_verified_task_number+'<br>'
	html += '待审核数量：'+unReviewed_number+'<br>'
	html += '<a href =\'http://60.195.40.162:8000/tagging/report2/\'>点我看近十日审核量变化曲线</a><br>'
	html += '<h3>今日工资结算情况</h3>'
	if str13:
		html +='工资系统已更新,请管理员核对情况'+'<br>'
		html += '<table width="500" border="1"> \
		  <tr> \
			<td><strong>ID</strong></td> \
			<td><strong>真实姓名</strong></td>\
			<td><strong>工资</strong></td>\
		  </tr>'
		for i in str13:
			html += "<tr>"
			html += "<td>" + i[0] + "</td>"
			html += "<td>" + i[1] + "</td>"
			html += "<td>" + i[2] + "</td>"
			html += "</tr>"
		html +='</table>'
	else:
		html +='今日管理员没有操作工资系统哦'

	html += '\
	<br><h3>今日活跃标注人员情况</h3><br>\
	<table width="500" border="1"> \
		  <tr> \
			<td><strong>ID</strong></td> \
			<td><strong>用户名</strong></td>\
			<td><strong>真实姓名</strong></td>\
			<td><strong>标注任务数</strong></td>\
		  </tr>'
		  
	for i in str9:
		html += "<tr>"
		html += "<td>" + i[0] + "</td>"
		html += "<td>" + i[1] + "</td>"
		html += "<td>" + i[2] + "</td>"
		html += "<td>" + i[3] + "</td>"
		html += "</tr>"
	html +='\
		</table>\
	 <br><h3>今日审核人员进度</h3><br>\
	<table width="500" border="1"> \
		  <tr> \
			<td><strong>ID</strong></td> \
			<td><strong>用户名</strong></td>\
			<td><strong>真实姓名</strong></td>\
			<td><strong>审核任务数</strong></td>\
		  </tr>\
	  '
	for i in str12:
		html += "<tr>"
		html += "<td>" + i[0] + "</td>"
		html += "<td>" + i[1] + "</td>"
		html += "<td>" + i[2] + "</td>"
		html += "<td>" + i[3] + "</td>"
		html += "</tr>"
	html +='\
		</table>\
	<br><h3>低一致率标注用户预警</h3><br>\
	<table width="500" border="1"> \
		  <tr> \
			<td><strong>ID</strong></td> \
			<td><strong>用户名</strong></td>\
			<td><strong>真实姓名</strong></td>\
			<td><strong>标注任务数</strong></td>\
			<td><strong>平均一致率</strong></td> \
		  </tr>\
	  '
	for i in str5:
		html += "<tr>"
		html += "<td>" + i[0] + "</td>"
		html += "<td>" + i[1] + "</td>"
		html += "<td>" + i[2] + "</td>"
		html += "<td>" + i[3] + "</td>"
		html += "<td>" + i[4] + "</td>"
		html += "</tr>"
	html +='\
		</table>\
	<br><h3>低一致率任务预警</h3>\
		<table width="500" border="1">\
		  <tr>\
			<td><strong>ID</strong></td>\
			<td><strong>任务名称</strong></td>\
			<td><strong>一致率</strong></td>\
			<td><strong>标注人员1</strong></td>\
			<td><strong>标注人员2</strong></td>\
		  </tr>\
	'
	
	for i in str6:
		html += "<tr>"
		html += "<td>" + i[0] + "</td>"
		html += "<td><a href='"+i[5]+"'>" + i[1] + "</a></td>"
		html += "<td>" + i[2] + "</td>"
		html += "<td>" + i[3] + "</td>"
		html += "<td>" + i[4] + "</td>"
		html += "</tr>"
	html +='\
		</table>\
	<br><h3>审核人员不确定选项统计</h3>\
		<table width="500" border="1">\
		  <tr>\
			<td><strong>ID</strong></td>\
			<td><strong>任务名称</strong></td>\
			<td><strong>审核人员</strong></td>\
			<td><strong>选择不确定的数量</strong></td>\
		  </tr>\
	'
	
	for i in str16:
		html += "<tr>"
		html += "<td>" + i[0] + "</td>"
		html += "<td><a href='"+i[4]+"'>" + i[1] + "</a></td>"
		html += "<td>" + i[2] + "</td>"
		html += "<td>" + i[3] + "</td>"
		html += "</tr>"
	html +="""
		</table>	
	</body>
	</html>
			"""
	
#	 发送邮件
	now_time = datetime.datetime.now().strftime('%Y%m%d')
	if argv1 == '1':
		yag.send(['bnuzgn@qq.com'],'['+now_time+']标注系统日报',contents = [html])
	elif argv1 == '2':
		yag.send(['621038800@qq.com','renli@putao.com','zhangjunbo@putao.com','bnuzgn@qq.com','122502325@qq.com','heyu@putao.com','tongzijian@putao.com','621038800@qq.com'],'['+now_time+']标注系统日报',contents = [html])
	
def echarts_plot(html_path,html2_path,col_1,row_1,col_2,row_2):
	'''绘图1'''
	line = Line("近十日标注量变化曲线", datetime.datetime.now().strftime('%Y-%m-%d'), width=1200, height=600)
	line.add("日期", row_1, col_1, mark_point=[ "max", "min"], mark_line=["average"],is_datazoom_show=True,is_symbol_show=True)
	line.render(path=html_path, pixel_ratio=3)
	'''绘图完成'''
	
	'''绘图2'''
	line = Line("近十日审核量变化曲线", datetime.datetime.now().strftime('%Y-%m-%d'), width=1200, height=600)
	line.add("日期", row_2, col_2 , mark_point=[ "max", "min"], mark_line=["average"],is_datazoom_show=True,is_symbol_show=True)
	line.render(path=html2_path, pixel_ratio=3)
	'''绘图完成'''
	
#sql的查询语句，年久失修，具体实现功能可以参考日报样例=、=
sql1 = 'SELECT count(*) from Tagging_event where event_type = 3 and TO_DAYS(Now()) = TO_DAYS(event_date)'	
sql2_2 = 'SELECT count(*)/(SELECT count(*) from Tagging_task where task_type=1)as totalNumber from Tagging_task where  task_type=1 AND (tagging_rate_2 = 1 or tagging_rate_1 =1 )'
sql2_1 = 'SELECT count(*) from Tagging_task where  task_type=1 AND (tagging_rate_2 = 1 or tagging_rate_1 =1 )'
sql3 = 'SELECT count(*) from Tagging_user where  id = any(select distinct user_id from Tagging_event WHERE event_type = 3 and TO_DAYS(Now())=TO_DAYS(event_date)) and task_num>=5'
sql4 = 'SELECT count(*) from Tagging_user where authority = 3'
sql5 = 'SELECT id,username,real_name,task_num,avg_same_rate from Tagging_user where avg_same_rate<0.7 and task_num >5 and authority = 3 ORDER BY avg_same_rate DESC'
sql6 = 'SELECT id, task_name,consistency_rate,tagging_user_1,tagging_user_2 from Tagging_task where tagging_rate_2 = 1 and tagging_rate_1 = 1 and task_type = 1 and is_ok=0 and consistency_rate<0.7 ORDER BY consistency_rate limit 30'
sql7 = 'SELECT count(*) from Tagging_event where event_type=5 and TO_DAYS(event_date) = TO_DAYS(Now())'
sql8 = 'SELECT count(*)/(SELECT count(*) from Tagging_task where tagging_rate_2=1 and tagging_rate_1=1 and task_type = 1) from Tagging_task where is_ok = 1'
sql9 = 'select Tagging_user.id , Tagging_user.username, Tagging_user.real_name, count(*) from Tagging_user inner join Tagging_event on Tagging_user.id = Tagging_event.user_id where TO_DAYS(Now()) = TO_DAYS(event_date) and event_type =3 GROUP BY user_id ORDER BY count(*) desc LIMIT 5'
sql10 = 'SELECT * FROM(SELECT count(*), event_date from Tagging_event where event_type = 3  GROUP BY event_date ORDER BY event_date DESC LIMIT 30) as table_1 order by table_1.event_date ASC'
sql11 = 'SELECT * from (SELECT count(*), event_date from Tagging_event where event_type = 5  GROUP BY event_date ORDER BY event_date DESC LIMIT 30)as table_1 ORDER by table_1.event_date ASC'
sql12 = 'select Tagging_user.id ,Tagging_user.username,Tagging_user.real_name,IFNULL(hhh.number,0) from Tagging_user left join (SELECT user_id,username,real_name,COUNT(*) as number from Tagging_user left join Tagging_event on Tagging_user.id = Tagging_event.user_id where Tagging_user.authority = 5 and event_type=5  and  TO_DAYS(Now()) = TO_DAYS(event_date) GROUP BY user_id ORDER BY count(*) DESC ) as hhh on Tagging_user.id = hhh.user_id where Tagging_user.authority=5 ORDER BY hhh.number desc'
sql13 = 'select Tagging_user.id, real_name, SUM(payoff_amount) from Tagging_payoff INNER jOIN Tagging_user on staff_id = Tagging_user.id  where TO_DAYS(NOW()) = TO_DAYS(payoff_date) GROUP BY Tagging_user.id'
sql14 = 'select count(*) from Tagging_task where tagging_rate_1=1 and tagging_rate_2=1  and is_ok = 0'
sql15 = 'select count(*) from Tagging_task where is_ok =0'
sql16 = 'select id,task_name,review_user,review_uncertain from Tagging_task where task_type=1 and is_ok=1 and id>\'2671\' order by review_uncertain desc limit 30'
sql = [sql1,sql2_1,sql2_2,sql3,sql4,sql5,sql6,sql7,sql8,sql9,sql10,sql11,sql12,sql13,sql14,sql15,sql16]

#用于从mysql返回结果中取出结果
pattern1 = re.compile('\((.*?),\)')
pattern2_1 = re.compile('\((.*?),\)')
pattern2_2 = re.compile('\(Decimal\(\'(.*?)\'\)\,\)')
pattern3 = re.compile('\((.*?),\)')
pattern4 = re.compile('\((.*?),\)')
pattern7 = re.compile('\((.*?),\)')
pattern8 = re.compile('\(Decimal\(\'(.*?)\'\)\,\)')
pattern14 = re.compile('\((.*?),\)')
pattern15 = re.compile('\((.*?),\)')
pattern16 = re.compile('\((.*?),\)')

#绘图保存地点
html_path = r'/home/tagging/web/TaggingSys/sb-admin/snapshot.html'
html2_path = r'/home/tagging/web/TaggingSys/sb-admin/snapshot2.html'

if __name__ == '__main__':
	argv1 = sys.argv[1]
	today_task_number = 0
	total_finished_task_number = 0
	proportion = 0
	today_active_number = 0
	total_tagging_people = 0
	today_verified_task_number = 0
	verified_proportion = 0
	unReviewed_number = 0
	total_verified_task_number = 0
	str5 = []
	str6 = []
	str9 = []
	str12 = []
	str13 = []
	str16 = []
	col_1 = []
	row_1 = []
	col_2 = []
	row_2 = []
	
	#在数据库所在机器配置
	try:
		db = pymysql.connect(host = "127.0.0.1",port = 3306,user = "root",passwd = "tagging",database = "TaggingSys" ) 
	except:
		time.sleep(2)
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
					total_finished_task_number = pattern2_1.findall(str(i))[0]
			else:
				pass
			
		if i is 2:
			ret = list(cursor.fetchall())
			if len(ret):
				for i in ret:
				   proportion = pattern2_2.findall(str(i))[0]
			else:
				pass
		if i is 3:
			ret = list(cursor.fetchall())
			if len(ret):
				for i in ret:
				   today_active_number = pattern3.findall(str(i))[0]
			else:
				pass
		if i is 4:
			ret = list(cursor.fetchall())
			if len(ret):
				for i in ret:
				   total_tagging_people = pattern4.findall(str(i))[0]
			else:
				pass
		if i is 5:
			ret = list(cursor.fetchall())
			if len(ret):
				for i in ret:
					temp = []
					for j in i:
#							print(temp)
						temp.append(str(j))
					str5.append(temp)
			else:
				pass
		if i is 6:
			ret = list(cursor.fetchall())
			if len(ret):
				for i in ret:
					temp2 =[]
					temp = []
					count = 0
					for j in i:
						
						if count is not 2:
							temp.append(j)
#								print(temp)
						temp2.append(str(j))
						count = count +1
					temp2.append('http://60.195.40.162:8000/tagging/data/?taskid='+str(temp[0])+'&taskname='+temp[1]+'')
					str6.append(temp2)
			else:
				pass
		if i is 7:
			ret = list(cursor.fetchall())
			if len(ret):
				for i in ret:
					today_verified_task_number = pattern7.findall(str(i))[0]
			else:
				pass
		if i is 8:
			ret = list(cursor.fetchall())
			if len(ret):
				for i in ret:
					verified_proportion = pattern8.findall(str(i))[0]
			else:
				pass
		if i is 9:
			ret = list(cursor.fetchall())
			if len(ret):
				for i in ret:
					temp = []
					for j in i:
#							print(temp)
						temp.append(str(j))
					str9.append(temp)
			else:
				pass
		if i is 10:
			ret = list(cursor.fetchall())
			if len(ret):
				for i in ret:
					for j in range(0,len(i)):
						if j==0:
							col_1.append(i[j])
						elif j==1:
							row_1.append(i[j])
				   
			else:
				pass
		if i is 11:
			ret = list(cursor.fetchall())
			if len(ret):
				for i in ret:
					for j in range(0,len(i)):
						if j==0:
							col_2.append(i[j])
						elif j==1:
							row_2.append(i[j])
				   
			else:
				pass
		if i is 12:
			ret = list(cursor.fetchall())
			if len(ret):
				for i in ret:
					temp = []
					for j in i:
#							print(temp)
						temp.append(str(j))
					str12.append(temp)
			else:
				pass
		if i is 13:
			ret = list(cursor.fetchall())
			if len(ret):
				for i in ret:
					temp = []
					for j in i:
#							print(temp)
						temp.append(str(j))
					str13.append(temp)
			else:
				pass
		if i is 14:
			ret = list(cursor.fetchall())
			if len(ret):
				for i in ret:
					unReviewed_number = pattern14.findall(str(i))[0]
			else:
				pass
		if i is 15:
			ret = list(cursor.fetchall())
			if len(ret):
				for i in ret:
					total_verified_task_number = pattern15.findall(str(i))[0]
			else:
				pass
		if i is 16:
			ret = list(cursor.fetchall())
			if len(ret):
				for i in ret:
					temp2 =[]
					temp = []
					count = 0
					for j in i:
						
						if count is not 2:
							temp.append(j)
#								print(temp)
						temp2.append(str(j))
						count = count +1
					temp2.append('http://60.195.40.162:8000/tagging/data/?taskid='+str(temp[0])+'&taskname='+temp[1]+'')
					str16.append(temp2)
			else:
				pass

	# 关闭数据库连接
	db.close()

	# 用于使用echarts绘制变化图片
	echarts_plot(html_path,html2_path,col_1,row_1,col_2,row_2)
	#将其余参数传至函数中生成html方便展示并发送邮件
	send_email(argv1,today_task_number,total_finished_task_number,proportion,today_active_number,total_tagging_people,str5,str6,today_verified_task_number,verified_proportion,str9,html_path,html2_path,str12,str13,str16,unReviewed_number,total_verified_task_number)
