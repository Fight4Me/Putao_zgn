# coding=utf-8
from __future__ import unicode_literals
from pyecharts import Line

html_path = r'C:\Users\bnuzgn\Desktop\snapshot.html'

cities =['1','2','3','4']
highs =['1','2','3','4']
line = Line("气温变化折线图", '2018-4-16', width=1200, height=600)
line.add("最高气温", cities, highs, mark_point=['average'], is_datazoom_show=True)
#line.add("最低气温", cities, lows, mark_line=['average'], is_smooth=True)
line.render(path=html_path, pixel_ratio=3)