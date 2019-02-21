# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 15:58:55 2019

@author: bnuzgn
"""
import pymysql
import yagmail
import datetime
from sshtunnel import SSHTunnelForwarder

def send_email1(retList):
	#链接邮箱服务器
    yag = yagmail.SMTP(user="zhangguannan@putao.com", password="Zmy64q2q83", host='smtp.putao.com')	
	#显示输出
    html = '<br><h3>语音标注不认真完成情况</h3><br>'
    html += '<table width="500" border="1"><tr>'
    html += '<td><strong>用户名</strong></td>'
    html += '<td><strong>姓名</strong></td>'
    html += '<td><strong>任务名</strong></td>'
    html += '<td><strong>耗时(分钟)</strong></td></tr>'
    for i in retList:
        html += "<tr>"
        html += "<td>" + i[0] + "</td>"
        html += "<td>" + i[1] + "</td>"
        html += "<td>" + i[2] + "</td>"
        html += "<td>" + str(i[3]/60) + "</td>"
        html += "</tr>"
    html+= '</table>'
    #	 发送邮件
    now_time = datetime.datetime.now().strftime('%Y%m%d%H')
    yag.send(['621038800@qq.com','renli@putao.com','bnuzgn@qq.com','heyu@putao.com'],'['+now_time+']标注系统偷懒预警',contents = [html])
    #yag.send(['bnuzgn@qq.com'],'['+now_time+']标注系统偷懒预警',contents = [html])
    
def send_email2(retList):
	#链接邮箱服务器
    yag = yagmail.SMTP(user="zhangguannan@putao.com", password="Zmy64q2q83", host='smtp.putao.com')	
	#显示输出
    html = '<br><h3>线上标注不认真完成情况</h3><br>'
    html += '<table width="500" border="1"><tr>'
    html += '<td><strong>用户名</strong></td>'
    html += '<td><strong>姓名</strong></td>'
    html += '<td><strong>任务名</strong></td>'
    html += '<td><strong>耗时(分钟)</strong></td></tr>'
    for i in retList:
        html += "<tr>"
        html += "<td>" + i[0] + "</td>"
        html += "<td>" + i[1] + "</td>"
        html += "<td>" + i[2] + "</td>"
        html += "<td>" + str(i[3]/60) + "</td>"
        html += "</tr>"
    html+= '</table>'
    #	 发送邮件
    now_time = datetime.datetime.now().strftime('%Y%m%d%H')
    yag.send(['621038800@qq.com','renli@putao.com','bnuzgn@qq.com','heyu@putao.com'],'['+now_time+']标注系统偷懒预警',contents = [html])
    #yag.send(['bnuzgn@qq.com'],'['+now_time+']标注系统偷懒预警',contents = [html])

if __name__ == '__main__':
	with SSHTunnelForwarder(('60.195.40.162',22),ssh_password="ZhiXue_tagging01",ssh_username="tagging",remote_bind_address=('127.0.0.1', 3306)) as server: 
		db = pymysql.connect(host = "127.0.0.1",port = server.local_bind_port,user = "root",passwd = "tagging",database = "TaggingSys" ) 
		sql1 = r'select Tagging_user.username,Tagging_user.real_name,new2.task_name,new2.timeDec from Tagging_user inner join (select * from Tagging_task inner join (select Tagging_event.user_id,Tagging_event.task_id,TIME_TO_SEC(new.event_time)-TIME_TO_SEC(Tagging_event.event_time)as timeDec from Tagging_event inner join (select * from Tagging_event where event_type=3 and TIME_TO_SEC(Now())-TIME_TO_SEC(event_time) <= 3600 and TO_DAYS(Now())=TO_DAYS(event_date))as new on Tagging_event.task_id=new.task_id and Tagging_event.user_id = new.user_id where Tagging_event.event_type=2 and TO_DAYS(Tagging_event.event_date)=TO_DAYS(new.event_date) and TIME_TO_SEC(new.event_time)-TIME_TO_SEC(Tagging_event.event_time)<6000 )as new1 on new1.task_id=Tagging_task.id)as new2 on Tagging_user.id=new2.user_id group by Tagging_user.username'
		sql2 = r'select Tagging_user.username,Tagging_user.real_name,new2.task_name,new2.timeDec from Tagging_user inner join (select * from Tagging_task inner join (select Tagging_event.user_id,Tagging_event.task_id,TIME_TO_SEC(new.event_time)-TIME_TO_SEC(Tagging_event.event_time)as timeDec from Tagging_event inner join (select * from Tagging_event where event_type=9 and TIME_TO_SEC(Now())-TIME_TO_SEC(event_time) <= 3600 and TO_DAYS(Now())=TO_DAYS(event_date))as new on Tagging_event.task_id=new.task_id and Tagging_event.user_id = new.user_id where Tagging_event.event_type=8 and TO_DAYS(Tagging_event.event_date)=TO_DAYS(new.event_date) and TIME_TO_SEC(new.event_time)-TIME_TO_SEC(Tagging_event.event_time)<6000 )as new1 on new1.task_id=Tagging_task.id)as new2 on Tagging_user.id=new2.user_id group by Tagging_user.username'
		sql3 = r'select count(*) from Tagging_event where event_type=9'
		cursor = db.cursor()
		cursor.execute(sql3)
		ret3=cursor.fetchall()
		print(ret3[0][0])
		cursor.execute(sql1)
		retList = list(cursor.fetchall())
		if retList:
			send_email1(retList)
		cursor.execute(sql2)
		retList2 = list(cursor.fetchall())
		if retList2:
			send_email2(retList2)
			