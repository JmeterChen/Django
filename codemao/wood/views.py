from django.shortcuts import render
from django.http import HttpResponse
import xlrd
from wood.models import *

from django.db.models import *
from django.db import connection

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


# def db_demo(request):
#
# 	# 清空数据库中四张表中所有数据
# 	Author.objects.all().delete()
# 	Book.objects.all().delete()
# 	AuthorDetail.objects.all().delete()
# 	Publisher.objects.all().delete()
#
# 	# get excle_object
# 	file = xlrd.open_workbook('./图书信息表.xls')
# 	sheet_author_detail = file.sheet_by_name('作者信息')
# 	sheet_publish = file.sheet_by_name('出版社信息')
# 	sheet_book = file.sheet_by_name('图书信息')
#
# 	# 首先从作者信息表取数据
# 	for i in range(1, sheet_author_detail.nrows):
# 		author_row_values = sheet_author_detail.row_values(i)
# 		author_name = author_row_values[0]
# 		# 补全Author表
# 		author = Author.objects.create(name=author_name)
# 		sex = 0
# 		if author_row_values[1] == '女':
# 			sex = 1
# 		elif author_row_values[1] == '男':
# 			sex = sex
# 		else:
# 			print('表中性别填写有误！')
# 		# 补全AuthorDetail表
# 		AuthorDetail.objects.create(author=author, sex=sex, age=author_row_values[2],
# 		                            email=author_row_values[3], phone=author_row_values[4])
#
# 	# 从出版社信息表取数据
# 	for i in range(1, sheet_publish.nrows):
# 		publish_row_values = sheet_publish.row_values(i)
# 		# 补全出版社信息表
# 		Publisher.objects.create(name=publish_row_values[0], address=publish_row_values[1], city=publish_row_values[2],
# 		                         website=publish_row_values[3])
#
# 	# 从图书信息表中取数据
# 	for i in range(1, sheet_book.nrows):
# 		book_row_values = sheet_book.row_values(i)
# 		publish_id = Publisher.objects.filter(name=book_row_values[2]).first().id
# 		# 补全图书表
# 		book = Book.objects.create(title=book_row_values[0], publisher_id=publish_id)
# 		# # 上面两行的代码可以换下面这种等价方式写
# 		# publish = Publisher.objects.filter(name=book_row_values[2]).first()
# 		# book = Book.objects.create(title=book_row_values[0], publisher=publish)
# 		if ',' in book_row_values[1]:
# 			name_list = book_row_values[1].split(',')
# 			for m in name_list:
# 				author = Author.objects.filter(name=m).first()
# 				book.authors.add(author)
# 		else:
# 			author = Author.objects.filter(name=book_row_values[1]).first()
# 			book.authors.add(author)
# 	return HttpResponse('所有数据均成功导入数据库！')


def db_demo(request):
	# # 以...开头
	# for a in (Author.objects.filter(name__startswith='杨')):
	# 	print(a.name)
	#
	# # 包含...内容
	# for i in (Book.objects.filter(title__contains='大学')):
	# 	print(i)
	
	# 在...范围内 区间
	# for i in (AuthorDetail.objects.filter(age__range=(20, 40))):
	# 	print(i.author.name, i.age)
		
	# # 断点存在于一个list范围内
	# for i in (AuthorDetail.objects.filter(age__in=[22, 24, 30, 33, 36, 39, 54, 26, 28])):
	# 	print(i.author.name, i.age)
	
	# # 返回一个新的 QuerySet，筛选条件不匹配的对象
	# for i in (AuthorDetail.objects.exclude(age__range=(20, 40))):
	# 	print(i.author.name, i.age)
	
	# # 排序 字段加负号"-"表示降序排序。默认是采用升序排序
	# for i in (AuthorDetail.objects.filter().order_by('-age')):
	# 	print(i.author.name, i.age)
	
	# # 反序排列
	# for i in (AuthorDetail.objects.filter()):
	# 	print(i)
	#
	# print('----------分界线-----------')
	# for i in (reversed(AuthorDetail.objects.filter())):
	# 	print(i)

	# for i in (AuthorDetail.objects.exclude(age=54)).values('author__name', 'age', 'sex'):
	# 	print(i)
	
	# for i in (AuthorDetail.objects.filter(age__range=(20, 30))).values('author'):
	# 	print(i['author'])
	#
	# for i in (Author.objects.filter(authordetail__age__range=(20, 30))).values('name'):
	# 	print(i['name'])

	# print(Book.objects.filter(title='21天放弃Python编程').values('authors__name', 'publisher__name'))
	
	# books = AuthorDetail.objects.filter(author__name='刘大海').values('author__book__title')
	# for i in books:
	# 	print(i['author__book__title'])
	
	# print(Book.objects.filter(publisher__name='高等教育').count())
	
	# print(Book.objects.filter(publisher__name='机械工业出版社').values('perice'))
	
	# # 算所有作者的平均年龄以及年龄总和
	# print(AuthorDetail.objects.all().aggregate(Avg('age'), Sum('age')))
	
	# # 算所有男性作者的平均年龄
	# print(AuthorDetail.objects.filter(sex='0').aggregate(Avg('age')))
	
	# # 找女性作者中最大年龄
	# print(AuthorDetail.objects.filter(sex='1').aggregate(Max('age')))
	
	cursor = connection.cursor()
	cursor.execute('select * from wood_book')
	print(cursor.fetchall())
	return HttpResponse(123)