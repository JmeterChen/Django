from django.shortcuts import render
from index.models import *
from django.http import HttpResponseRedirect
# Create your views here.


def index(request):
	students = Students.objects.all()
	# print(students)
	return render(request, 'index.html', {'student': students, 'flag': 0})


def demo(request):
	return render(request, 'demo_huice.html')


def login(request):
	return render(request, 'login.html')


def register(request):
	return render(request, 'register.html')


def api_login(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	if username and password:
		user = Users.objects.filter(username=username, password=password)
		if user:
			return render(request, 'home.html', {'username': username})
		else:
			return render(request, 'error.html', {'msg': '用户名或密码错误！'})
		
	else:
		return render(request, 'error.html', {'msg': '缺少必填参数：username or password!'})
	
	
def api_register(request):
	username = request.POST.get('username')
	email = request.POST.get('email')
	pass_s = request.POST.get('pass_s')
	if username and email and pass_s:
		if not Users.objects.filter(username=username).exists():
			try:
				Users.objects.create(username=username, email=email, password=pass_s)
				return HttpResponseRedirect('/index/login/')
			except:
				return render(request, 'error.html', {"msg": "数据库未知错误！"})
		else:
			return render(request, 'error.html', {'msg': '此用户已存在！'})
		
	else:
		return render(request, 'error.html', {'msg': '缺少必填参数：username or password or email!'})