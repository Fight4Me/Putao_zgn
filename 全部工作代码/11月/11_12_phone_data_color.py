# -*- coding: utf-8 -*-
import xlrd
import os
import re

def excel_2_txt():
    workbook = xlrd.open_workbook(r'C:\Users\bnuzgn\Desktop\sentence prone  Hannah.xlsx',formatting_info=True)
#    print(workbook.sheet_names())
    sheet = workbook.sheet_by_name('Sheet1')
    formatIndex = sheet.cell_xf_index(0, 3)
    format = workbook.computed_xf_list[formatIndex]
    font = workbook.font_list[format.font_index]
    color = workbook.colour_map[font.colour_index]
    print(color)

if __name__ == '__main__':
    excel_2_txt()