from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.http import JsonResponse
from wood.models import *

# Create your views here.


def home(request):
	return render(request, 'current_datetime.html')


def demo(request):
	# Author(first_name="Chen", last_name="Bolin").save()
	# AuthorDetail(sex=0, age=50, email='chenbolin@qq.com', phone='11111', author_id=1).save()
	author1 = Author(first_name="陈", last_name="文建")
	author1.save()
	AuthorDetail(sex=0, age=50, email='chenbolin@qq.com', phone='11111', author_id=author1.id).save()
	return HttpResponse(123)


def bad_page(request):
	# return HttpResponse("Welcome to the page at /current/")
	return HttpResponse("Welcome to the page at %s" % request.path)

# def demo2(request):
# 	author = Author(first_name="陈", last_name="文建", email='chenwenjian@qq.com')
# 	author.save()
# 	# print(author)
# 	AuthorDetail(sex=0, age=50, email='chenbolin@qq.com', phone='11111', author_id=2).save()
# 	return HttpResponse(123)
#
#
# def demo3(request):
# 	author = Author(first_name="科", last_name="比", email='kobe@qq.com')
# 	author.save()
# 	AuthorDetail(sex=0, age=50, email='kobe@qq.com', phone='2222', author_id=author).save()
# 	return HttpResponse(123)


def year_today(request, year):
	return HttpResponse('The moment Year is %s' % year)


def month_today(request, year, month):
	return HttpResponse('The moment month is %s ,The Year is %s' % (month, year))


def delete_author(request):
	# author = Author.objects.filter(first_name='Chen')
	# print(type(author))
	# b = Book.objects.all()
	# print(type(b))
	author = Author.objects.all()[0]
	return HttpResponse(author.first_name)