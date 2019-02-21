# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 11:54:05 2018

@author: bnuzgn
"""

from __future__ import unicode_literals
import pymysql
from sshtunnel import SSHTunnelForwarder

if __name__ == '__main__':
	with SSHTunnelForwarder(('60.195.40.162',22),ssh_password="ZhiXue_tagging01",ssh_username="tagging",remote_bind_address=('127.0.0.1', 3306)) as server: 
		db = pymysql.connect(host = "127.0.0.1",port = server.local_bind_port,user = "root",passwd = "tagging",database = "TaggingSys" ) 
		# 使用 cursor() 方法创建一个游标对象 cursors
		sql1 ='update Tagging_task inner join (select event2.task_id,event2.user_id,event2.tagging_user_1,real_name from (select task_id,user_id,tagging_user_1 from Tagging_event inner join (select * from Tagging_task where tagging_rate_1<>1 and task_type=1 and tagging_user_1 is not Null)as task on task.id=Tagging_event.task_id where Tagging_event.event_type=2 and TO_DAYS(Now())-TO_DAYS(Tagging_event.event_date)>1)as event2 inner join Tagging_user on event2.tagging_user_1=Tagging_user.username where event2.user_id=Tagging_user.id order by task_id)as list on list.task_id = Tagging_task.id set Tagging_task.tagging_user_1=Null'
		sql2 ='update Tagging_task inner join (select event2.task_id,event2.user_id,event2.tagging_user_2,Tagging_user.real_name from (select task_id,user_id,tagging_user_2 from Tagging_event inner join (select * from Tagging_task where tagging_rate_2<>1 and task_type=1 and tagging_user_2 is not Null)as task on task.id=Tagging_event.task_id where Tagging_event.event_type=2 and TO_DAYS(Now())-TO_DAYS(Tagging_event.event_date)>1) as event2 inner join Tagging_user on event2.tagging_user_2=Tagging_user.username where event2.user_id=Tagging_user.id order by task_id)as list on list.task_id = Tagging_task.id set Tagging_task.tagging_user_2=Null'
		sql = [sql1,sql2]
		cursor = db.cursor()
		for i in range(0,len(sql)):
			try:
				cursor.execute(sql[i]) 
				db.commit()
			except:
				db.rollback()
		db.close()