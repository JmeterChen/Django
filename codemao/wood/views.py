from django.shortcuts import render
from django.http import HttpResponse
import xlrd
from wood.models import *


# Create your views here.


def login(request):
	return HttpResponse(123)


# 作废,垃圾代码
# def db_test(request):
# 	workbook = xlrd.open_workbook('./图书信息表.xls')
# 	sheet = workbook.sheet_by_name('作者信息')
#
# 	for i in range(1, sheet.nrows):
# 		author_name = sheet.row_values(i)[0]
# 		Author.objects.create(name=author_name)
# 	return HttpResponse(123)
#
#
# # 通过接口把excle表中的出版社信息插入数据库
# def add_publisher(request):
# 	publish = xlrd.open_workbook('./图书信息表.xls')
# 	sheet_publish = publish.sheet_by_name('出版社信息')
# 	for i in range(1, sheet_publish.nrows):
# 		publish = sheet_publish.row_values(i)
# 		Publisher.objects.create(name=publish[0], address=publish[1], city=publish[2],
# 		                         website=publish[3])
# 	return HttpResponse('出版社信息已经插入数据库')
#
#
# # 通过接口把excle表中的作者详情信息插入数据库
# def add_author_detail(request):
# 	author_detail = xlrd.open_workbook('./图书信息表.xls')
# 	sheet_author_detail = author_detail.sheet_by_name('作者信息')
# 	for i in range(1, sheet_author_detail.nrows):
# 		author_detail = sheet_author_detail.row_values(i)
# 		AuthorDetail.objects.create(sex=author_detail[1],
# 		                            age=author_detail[2], email=author_detail[3],
# 		                            phone=author_detail[4])
# 	return HttpResponse('作者详情信息已经插入数据库')


def db_demo(request):
	
	# 清空数据库中四张表中所有数据
	Author.objects.all().delete()
	Book.objects.all().delete()
	AuthorDetail.objects.all().delete()
	Publisher.objects.all().delete()

	# get excle_object
	file = xlrd.open_workbook('./图书信息表.xls')
	sheet_author_detail = file.sheet_by_name('作者信息')
	sheet_publish = file.sheet_by_name('出版社信息')
	sheet_book = file.sheet_by_name('图书信息')

	# 首先从作者信息表取数据
	for i in range(1, sheet_author_detail.nrows):
		row_values = sheet_author_detail.row_values(i)
		author_name = row_values[0]
		# 补全Author表
		author = Author.objects.create(name=author_name)
		if row_values[1] == '女':
			sex = 1
		elif row_values[1] == '男':
			sex = 0
		else:
			print('表中性别填写有误！')
		# 补全AuthorDetail表
		AuthorDetail.objects.create(author=author, sex=1,
		                            age=row_values[2], email=row_values[3],
		                            phone=row_values[4])

	# 从出版社信息表取数据
	for i in range(1, sheet_publish.nrows):
		publish = sheet_publish.row_values(i)
		Publisher.objects.create(name=publish[0], address=publish[1], city=publish[2],
		                         website=publish[3])
		
		
	# 从图书信息表中取数据
	for i in range(1,sheet_book.nrows):
		book = sheet_book.row_values(i)
		Book.objects.create()

	return HttpResponse('所有数据均成功导入数据库！')