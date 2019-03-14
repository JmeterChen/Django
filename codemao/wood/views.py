from django.shortcuts import render
from django.http import HttpResponse
import xlrd
from wood.models import *

# Create your views here.


def login(request):
	return HttpResponse(123)


def db_test(request):
	workbook = xlrd.open_workbook('./图书信息表.xls')
	sheet = workbook.sheet_by_name('作者信息')
	
	for i in range(1, sheet.nrows):
		author_name = sheet.row_values(i)[0]
		Author.objects.create(name=author_name)
	return HttpResponse(123)