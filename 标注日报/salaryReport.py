# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 11:37:15 2018

@author: bnuzgn
用于生成excel日报，
虽然使用多个generate_excel函数，但仅用于生成多个sheet表，最后还是生成一个excel文件。
"""
import datetime
import pymysql
from sshtunnel import SSHTunnelForwarder
import re
import os
import xlwt

#用于mysql查询，其中510000是财务那边的要求，建议修改时不要变动，目的是保证每个人有一个固定的以51开头的ID
sql_1 = 'select LPAD(Tagging_user.id,6,\'510000\')as number,Tagging_user.real_name,Tagging_user.identify,Tagging_user.bank_card_num,Tagging_user.bank_name,Tagging_user.bank_city,Tagging_payoff.payoff_amount,Tagging_payoff.qualified_num,Tagging_payoff.unit_price from Tagging_user inner join Tagging_payoff on Tagging_user.id = Tagging_payoff.staff_id where month(NOW()) = month(Tagging_payoff.payoff_date) and Tagging_user.is_submit_info = 1 and Tagging_payoff.payoff_type = 1 order by number ASC'
sql_2 = 'select LPAD(Tagging_user.id,6,\'510000\')as number,Tagging_user.real_name,Tagging_user.identify,Tagging_user.bank_card_num,Tagging_user.bank_name,Tagging_user.bank_city,Tagging_payoff.payoff_amount,Tagging_payoff.qualified_num,Tagging_payoff.unit_price from Tagging_user inner join Tagging_payoff on Tagging_user.id = Tagging_payoff.staff_id where month(NOW()) = month(Tagging_payoff.payoff_date) and Tagging_user.is_submit_info = 1 and Tagging_payoff.payoff_type = 2 order by number ASC'
sql_3 = 'select LPAD(Tagging_user.id,6,\'510000\')as number,Tagging_user.real_name,Tagging_user.identify,Tagging_user.bank_card_num,Tagging_user.bank_name,Tagging_user.bank_city,Tagging_payoff.payoff_amount,Tagging_payoff.qualified_num,Tagging_payoff.unit_price from Tagging_user inner join Tagging_payoff on Tagging_user.id = Tagging_payoff.staff_id where month(NOW()) = month(Tagging_payoff.payoff_date) and Tagging_user.is_submit_info = 1 and Tagging_payoff.payoff_type = 3 order by number ASC'
save_path = r'./salaryData/'
#save_path = r'./'

def get_data(sql):
    db = pymysql.connect(host = "127.0.0.1" ,user = "root",passwd = "tagging",database = "TaggingSys" ) 
    # 使用 cursor() 方法创建一个游标对象 cursors
    cursor = db.cursor()
    cursor.execute(sql)
    ret = list(cursor.fetchall())
    return ret
def generate_excel(ret,wbk,sheet_name):
    sheet = wbk.add_sheet(sheet_name,cell_overwrite_ok=True)
    title = ['编号','姓名','身份证号','银行卡号','银行卡开户行','开户行所在城市','税前薪资','通过任务数','单价']
    for i in range(0,len(title)):
        sheet.write(0,i,title[i])
    for i in range(0,len(ret)):
        #对result的每个子元素作遍历，
        for j in range(0,len(ret[i])):
            #将每一行的每个元素按行号i,列号j,写入到excel中。
            sheet.write(i+1,j,ret[i][j])
    now_time = datetime.datetime.now().strftime('%Y%m%d')
    wbk.save(os.path.join(save_path,str(now_time)+'.xls'))

def generate_excel2(ret,wbk,sheet_name):
    sheet = wbk.add_sheet(sheet_name,cell_overwrite_ok=True)
    title = ['编号','姓名','身份证号','银行卡号','银行卡开户行','开户行所在城市','税前薪资','推荐数量','单价']
    for i in range(0,len(title)):
        sheet.write(0,i,title[i])
    for i in range(0,len(ret)):
        #对result的每个子元素作遍历，
        for j in range(0,len(ret[i])):
            #将每一行的每个元素按行号i,列号j,写入到excel中。
            sheet.write(i+1,j,ret[i][j])
    now_time = datetime.datetime.now().strftime('%Y%m%d')
    wbk.save(os.path.join(save_path,str(now_time)+'.xls'))

if __name__ == '__main__':
    wbk = xlwt.Workbook()
    table_list_1 = get_data(sql_1)
    generate_excel(table_list_1,wbk,'标注')
    table_list_2 = get_data(sql_2)
    generate_excel(table_list_2,wbk,'审核')
    table_list_3 = get_data(sql_3)
    generate_excel2(table_list_3,wbk,'奖金')
