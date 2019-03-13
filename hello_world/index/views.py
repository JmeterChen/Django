from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.views.decorators.http import require_http_methods
from datetime import datetime
import json
from django.http import JsonResponse
import os
import csv
from django.template.loader import get_template
from django.template import Context,Template

# Create your views here.


def login(request):
	# return render(request,'login.html')
	# 如果有cookie且正确，直接返回到home页面
	username = request.COOKIES.get('username')
	# pwd = request.COOKIES.get('password')
	# 因为is_login接口里面cookie中密码加密的方式改了，这里获取的时候方法也需要相应变更
	pwd = request.get_signed_cookie('password',default=None)
	print(pwd)
	with open('user.csv','r',encoding='utf-8') as f:
		reader = csv.reader(f)
		for i in reader:
			# print(i)
			# if username == 'admin' and pwd == '123456':
			if i[0] == username and i[1] == pwd:
				res = render(request, 'home.html', {'user':username})
				return res
		else:
			return render(request,'login.html')


def is_login(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	is_save = request.POST.get('is_save')
	print(is_save)
	if username and password:
		with open('user.csv','r',encoding='utf-8') as f:
			reader = csv.reader(f)
			for i in reader:
				# print(i)
				if i[0] == username and i[1] == password:
					res = render(request, 'home.html',{'user':username})
					if is_save =='on':
						res.set_cookie(key='username', value=username)
						# res.set_cookie(key='password', value=password)
						# django自带hash散列算法加密 这里改了，那么前面的login接口也要更改
						res.set_signed_cookie(key='password', value=password)
					return res
			else:
				# return HttpResponse('用户名或密码错误！')
				return render(request, 'error.html', {'msg': '用户名或密码错误！'})
	else:
		# return HttpResponse('缺少必填参数！')
		return render(request,'error.html', {'msg': '缺少必填参数！'})






bus_cal = {
			"business_autoFans_J": [{"2016_08": 14},  {"2016_09": 15}, {"2016_10" : 9}],
			"autoAX": [{"2016_08": 7},  {"2016_09": 32}, {"2016_10": 0}],
			"autoAX_admin": [{"2016_08": 5},  {"2016_09": 13}, {"2016_10": 2}],
		}

#
# def bugs_num(request):
# 	# 方法类型
# 	if request.method == 'GET':
# 		month = request.GET.get('month')
# 		# 参数必填
# 		if month:
# 			month = eval(month)
# 			# 参数有效
# 			if type(month) == int and month >= 1 and month <= 12:
# 				# bug_list = []
# 				bug_num = 0
# 				for m, n in bus_cal.items():
# 					for i in n:
# 						for m,n in i.items():
# 							if int(m[-2:]) == month:
# 								bug_num += n
# 				return HttpResponse(bug_num)
# 			else:
# 				return render(request,'error.html',{'msg':'请求参数无效！'})
# 		else:
# 			return render(request,'error.html',{'msg':'缺少必填参数！'})
# 	else:
# 		return render(request,'error.html',{'msg':'请求方法有误！'})


# @require_http_methods(["GET"])
# def bugs_num(request):
# 	month = request.GET.get('month')
# 	# 参数必填
# 	if month:
# 		month = eval(month)
# 		# 参数有效
# 		if type(month) == int and month >= 1 and month <= 12:
# 			# bug_list = []
# 			bug_num = 0
# 			for m, n in bus_cal.items():
# 				for i in n:
# 					for m,n in i.items():
# 						if int(m[-2:]) == month:
# 							bug_num += n
# 			return HttpResponse(bug_num)
# 		else:
# 			return render(request,'error.html',{'msg':'请求参数无效！'})
# 	else:
# 		return render(request,'error.html',{'msg':'缺少必填参数！'})

@require_http_methods(["GET"])
def bugs_num(request):
	month = request.GET.get('month')
	# 参数必填
	if month:
		month = eval(month)
		# 参数有效
		if type(month) == int and month >= 1 and month <= 12:
			# bug_list = []
			bug_num = 0
			for m, n in bus_cal.items():
				for i in n:
					for m,n in i.items():
						if int(m[-2:]) == month:
							bug_num += n
			# return HttpResponse('%s月bug 总数为： %d' %(month, bug_num))
			data = {"month": month, "bug总数为":bug_num}
			# return HttpResponse(content='{"month": %s, "bug总数为":%d}'%(month,bug_num),content_type='application/json')
			# # 这里可以conten可以用两种写法，法1：内容直接是上面字符串形式；法2：使用下面json.dunmps序列化
			# return HttpResponse(content=json.dumps(data),content_type='application/json')
		else:
			# return render(request,'error.html',{'msg':'请求参数无效！'})
			data = {"month":month,"msg":"请求参数无效！"}
			# return HttpResponse(content=json.dumps(data),content_type='application/json')
	else:
		# return render(request,'error.html',{'msg':'缺少必填参数！'})
		data = {"month":month,"msg":"缺少必填参数！"}
		# return HttpResponse(content=json.dumps(data),content_type='application/json')
	# 代码优化，使用这一行可以让上面的所有其他情况的代码被注释
	# return HttpResponse(content=json.dumps(data),content_type='application/json')
	# 这里还可以继续优化，直接使用JsonResponse库,参数放入字典即可
	return JsonResponse(data=data)


#  使用HttpResponnse返回字符串
def current_date(request):
	now_time = datetime.now()
	# html = "<html><body>Current time is: %s</body></html>" % now_time
	print(os.getcwd())
	cur_path = os.getcwd()
	fp = open('%s/demo.html' % cur_path,encoding='utf-8')
	t = Template(fp.read())
	fp.close()
	html = t.render(Context({'current_date': now_time}))
	return HttpResponse(html)


def app_current_date(request):
	now_time = datetime.now()
	# html = "<html><body>Current time is: %s</body></html>" % now_time
	print(os.getcwd())
	cur_path = os.getcwd()
	fp = open('%s/index/templates/app_demo.html' % cur_path, encoding='utf-8')
	t = Template(fp.read())
	fp.close()
	html = t.render(Context({'current_date': now_time}))
	return HttpResponse(html)


def now_time(request):
	# 单纯打印动态内容
	# return HttpResponse('Current time is : %s'%(datetime.now()))
	now_date = datetime.now()
	print(now_date)
	text = get_template('now_time.html')
	# msg = text.render(Context({'current_date':now_date}))  # 这里这样写会报错的
	msg = text.render({'current_date':now_date})
	return HttpResponse(msg)



def page_num(request,num):
	# # 从urls中获取参数内容，打印动态内容
	# return HttpResponse('Current page_num is: %s'%num)
	# 从urls中获取参数内容，传递给模板
	return render(request,'book.html',{'num':num})

def page_up(request,num):
	return render(request,'book.html',{'num':num-1})

def page_down(request,num):
	return render(request,'book.html',{'num':num+1})