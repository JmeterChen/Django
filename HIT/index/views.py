#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from models import *
import json

def home(request):
    return render(request, 'home.html', {'flag':True, 'students':[{'id':1, 'name':'张三', 'salary':6000},
							{'id':2, 'name':'田老师', 'salary':7500},
							{'id':3, 'name':'李四', 'salary':10000}
												 ]
						})

def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def user_check(request):
    name = request.GET.get('name')
    if name:
        if User.objects.filter(name=name).exists():
            return JsonResponse({"valid": False})
    return JsonResponse({"valid": True})

# def api_login(request):
# 	username = request.POST.get('username')
# 	password = request.POST.get('password')
# 	if username and password:
# 		if len(username) in range(5, 21) and len(password) in range(5, 11):
# 			user = User.objects.filter(name=username, password=password)
# 			if user.exists():
# 				return HttpResponse('登录成功')
# 			else:
# 				return render(request, 'error.html', {'info': '用户名或密码错误', 'url':'/index/login/'})
# 		else:
# 			return render(request, 'error.html', {'info': '用户名或密码长度错误'})
# 	else:
# 		return render(request, 'error.html', {'info': '用户名或为空'})


def api_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username and password:
        if len(username) in range(5, 21) and len(password) in range(5, 11):
            user = User.objects.filter(name=username, password=password)
            if user.exists():
                return HttpResponse(content_type='application/json', content=json.dumps({'flag':0}))
            else:
                return HttpResponse(content_type='application/json', content=json.dumps({'flag': 1, 'msg': '用户名或密码错误'}))
        else:
            return HttpResponse(content_type='application/json', content=json.dumps({'flag': 1, 'msg': '用户名或密码长度错误'}))
    else:
        return HttpResponse(content_type='application/json', content=json.dumps({'flag': 1, 'msg': '用户名或密码为空'}))


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})


def search_task(request):
    name = request.GET.get('name')
    if name:
        tasks = Task.objects.filter(name__contains=name)
        li = []
        if tasks.exists():
            for task in tasks:
                li.append({'id': task.id, 'name':task.name, 'desc':task.desc})
        return HttpResponse(content_type='application/json', content=json.dumps({'tasks': li}))
    else:
        tasks = Task.objects.all()
        li = []
        for task in tasks:
            li.append({'id': task.id, 'name': task.name, 'desc': task.desc})
        return HttpResponse(content_type='application/json', content=json.dumps({'tasks': li}))


def task_new(request):
    return render(request, 'task_new.html')


def api_task_new(request):
    name = request.POST.get('name')
    desc = request.POST.get('desc')
    tasks = Task.objects.filter(name=name)
    if not tasks.exists():
        Task.objects.create(name=name, desc=desc)
    return HttpResponseRedirect('/index/task/list/')

