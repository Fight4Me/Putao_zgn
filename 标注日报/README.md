# 日报系统

1.  “12_10_dalilyReport(旧).py”用于旧任务的每日日报，包含自动邮件、绘图、查询数据库功能的结合，结合crontab可查询当日的信息并且以邮件的形式发送出去。
2.  “salaryReport.py、salaryMail.py” 用于生成当月的工资情况，并以邮件的形式发送出去，实现方式与日报相同。均需要结合crontab。
3.  “segDailyReport.py”用于切分任务日报工作。