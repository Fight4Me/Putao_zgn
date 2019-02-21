# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 12:45:46 2018

@author: bnuzgn
"""

import yagmail
import datetime
import pymysql
from sshtunnel import SSHTunnelForwarder
import re

def send_email(today_task_number,total_finished_task_number,proportion,today_active_number,total_tagging_people,str5,str6):
    #链接邮箱服务器
    yag = yagmail.SMTP(user="zhangguannan@putao.com", password="Zmy64q2q83", host='smtp.putao.com')
    
    #邮箱正文
#    contents5 =today_task_number+'\n'+total_finished_task_number+'\n'+proportion+'\n'+today_active_number+'\n'+total_tagging_people+'\n'+str5+'\n'+str6
    
    html = '<html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /></head><body>'    
    html += '当日标注完成数量：'+today_task_number+'<br>'
    html += '已完成标注量：'+total_finished_task_number+'<br>'
    html += '已完成标注量占总量比重：'+proportion+'<br>'
    html += '今日活跃人数：'+today_active_number +'<br>'+ '\
    总标注人数：'+total_tagging_people+'<br>'+'<br>'+'\
       <table width="500"> \
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
        <table width="500">\
          <tr>\
            <td><strong>ID</strong></td>\
            <td><strong>任务名称</strong></td>\
            <td><strong>一致率</strong></td>\
          </tr>\
    '
    for i in str6:
        html += "<tr>"
        html += "<td>" + i[0] + "</td>"
        html += "<td><a href='"+i[3]+"'>" + i[1] + "</a></td>"
        html += "<td>" + i[2] + "</td>"
        html += "</tr>"
    html +="""
        </table>
    </body>
    </html>
            """
    
#     发送邮件
    now_time = datetime.datetime.now().strftime('%Y%m%d')
    yag.send(['bnuzgn@qq.com'],'['+now_time+']标注系统日报',contents = [html])
#    yag.send(['bnuzgn@qq.com','122502325@qq.com','heyu@putao.com','tongzijian@putao.com'], 'subject',contents = [contents,html])
sql1 = 'SELECT count(*) from Tagging_event where event_type = 3 and TO_DAYS(Now()) = TO_DAYS(event_date)'    
sql2_2 = 'SELECT count(*)/(SELECT count(*) from Tagging_task where task_type=1)as totalNumber from Tagging_task where  task_type=1 AND (tagging_rate_2 = 1 or tagging_rate_1 =1 )'
sql2_1 = 'SELECT count(*) from Tagging_task where  task_type=1 AND (tagging_rate_2 = 1 or tagging_rate_1 =1 )'
sql3 = 'SELECT count(*) from Tagging_user where  id = any(select distinct user_id from Tagging_event WHERE event_type = 3 ) and task_num>=5'
sql4 = 'SELECT count(*) from Tagging_user where authority = 3'
sql5 = 'SELECT id,username,real_name,task_num,avg_same_rate from Tagging_user where avg_same_rate<0.8 and task_num >5 and authority = 3'
sql6 = 'SELECT id, task_name,consistency_rate from Tagging_task where tagging_rate_2 = 1 and tagging_rate_1 = 1 and task_type = 1 and consistency_rate<0.75'
sql = [sql1,sql2_1,sql2_2,sql3,sql4,sql5,sql6]

pattern1 = re.compile('\((.*?),\)')
pattern2_1 = re.compile('\((.*?),\)')
pattern2_2 = re.compile('\(Decimal\(\'(.*?)\'\)\,\)')
pattern3 = re.compile('\((.*?),\)')
pattern4 = re.compile('\((.*?),\)')

if __name__ == '__main__':
    today_task_number = 0
    total_finished_task_number = 0
    proportion = 0
    today_active_number = 0
    total_tagging_people = 0
    str5 = []
    str6 = []
    with SSHTunnelForwarder(('193.112.75.135',22),ssh_password="zhangguannan",ssh_username="zhangguannan",remote_bind_address=('127.0.0.1', 3306)) as server: 
        db = pymysql.connect(host = "127.0.0.1",port = server.local_bind_port,user = "root",passwd = "putao",database = "TaggingSys" ) 
        # 使用 cursor() 方法创建一个游标对象 cursors
        cursor = db.cursor()
        for i in range(0,7):
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
#                            print(temp)
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
#                                print(temp)
                            temp2.append(str(j))
                            count = count +1
                        temp2.append('http://193.112.75.135:8000/tagging/data/?taskid='+str(temp[0])+'&taskname='+temp[1]+'')
                        str6.append(temp2)
                else:
                    pass
#        print(taskLink)
#        print(str6)
        # 关闭数据库连接
        db.close()
        send_email(today_task_number,total_finished_task_number,proportion,today_active_number,total_tagging_people,str5,str6)