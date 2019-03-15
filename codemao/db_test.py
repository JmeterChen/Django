# -*- coding: utf-8 -*-#
# __author__ = 'Bo_lin Chen'
# Date: 2019/3/14

"""

python 操作excle

1、读取内容   xlrd库

2、写入内容   xlwt库
"""

# workbook

import xlrd

workbook = xlrd.open_workbook('./图书信息表.xls')
# print(type(workbook))
sheet_name_list = workbook.sheet_names()
# print(sheet_name_list)



# #
# # # sheet 方法
# #
# # # 返回指定打开的excle中的所有页签名称列表
# # print(workbook.sheet_names())  # ['作者信息', '出版社信息', '图书信息']
# #
# # #
# sheet_author = workbook.sheet_by_name('作者信息')
# #
# # 整行 sheet.row()根据行号取行对象
# # print(sheet.row(1))
# print(sheet_author.row_values(1))
# #
# # # 根据行条件取行值
# # print('该表格中第1行的单元格内容文本是：%s' % sheet.row_values(0))
# #
# # # 根据行条件查询该行有多少列
# print('该表格中第一行有%s列' % sheet_author.row_len(0))
# #
# # # 查询有多少行 (备注，表内容中插入空行也会被算进去)
# print('该表中一共有 %s行' % sheet_author.nrows)
# #
# # for i in range(1, sheet_author.nrows):
# # 	print(sheet.row_values(i))
# #
# # # 取列
# # print('该表格中第4列的单元格内容文本是：%s' % sheet.col_values(3))
# #
# # # 查询有多少列
# print('该表格一共有%s列' % sheet_author.ncols)
# #
# # # 取单元格
# # a = sheet_author.cell(3, 3)
# print('该表格中第4行第4列的单元格内容是：%s' % sheet_author.cell(3, 3))
# # print(type(a))
# # print('该表格中第4行第4列的单元格内容是：%s' % a)
# # # print(dir(a))
# #
# # # 取单元格内容
# # # 方法1
# print('该表格中第4行第4列的单元格内容文本是：%s' % sheet_author.cell(3, 3).value)
# #
# # # 方法2
# print('该表格中第4行第4列的单元格内容文本是：%s' % sheet_author.cell_value(3, 3))
#
#
# # workbook = xlrd.open_workbook('./图书信息表.xls')
# # sheet = workbook.sheet_by_name('作者信息')
# #
# # for i in range(1, sheet.nrows):
# # 	print(sheet.row_values(i)[0])
#
# print('该表格第3列内容文本是：%s ' %sheet_author.col_values(2))
#
# print(sheet_author.ncols)


# # 出版社信息
# publish = xlrd.open_workbook('./图书信息表.xls')
# sheet_publish = publish.sheet_by_name('出版社信息')
# for i in range(1, sheet_publish.nrows):
# 	publish = sheet_publish.row_values(i)
# 	# print(publish)
# 	print(publish[0], publish[1], publish[2], publish[3])


# 作者详情
author_detail = xlrd.open_workbook('./图书信息表.xls')
sheet_author_detail = author_detail.sheet_by_name('作者信息')
for i in range(1, sheet_author_detail.nrows):
	author_detail = sheet_author_detail.row_values(i)
	print(author_detail)





