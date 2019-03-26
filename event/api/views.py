from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
# Create your views here.
from api.models import *
import time
from django.contrib import auth
from rest_framework.authtoken.models import Token
from django.db import connection

# def add_event(request):
# 	Event.objects.create(title='111', limit='50', status='0', address='深圳',
# 	                     times='2019-03-24')
# 	return HttpResponse(123)


@require_http_methods(["POST"])
def add_event(request):
	title = request.POST.get('title')
	limit = request.POST.get('limit', 200)
	status = request.POST.get('status', 0)
	address = request.POST.get('address')
	times = request.POST.get('times')
	if title and address and times:
		if not Event.objects.filter(title=title).exists():
			try:
				limit = int(limit)
				status = int(status)
				if status in [0, 1, 2]:
					try:
						time.strptime(times, '%Y-%m-%d %H:%M:%S')
					except:
						result = {'msg': '时间格式错误'}
					else:
						try:
							print(title, limit, status, address, times, type(times))
							event = Event.objects.create(title=title, limit=limit, status=status,
														 address=address, times=times)
							result = {
								"error_code": 0,
								"data": {
								"event_id": str(event.id),
								"status": str(status),
								}
							}
						except:
							result = {'msg': '数据库未知错误'}
				else:
					result = {'error_code': 10003}
			except:
				result = {'msg': 'limit或status字段不是纯数字'}
		else:
			result = {'error_code': 10002}
	else:
		result = {'error_code': 10001}
	return JsonResponse(result)


# @require_http_methods(['POST'])
# def add_guess(request):
# 	event_id = request.POST.get('id')
# 	name = request.POST.get('name')
# 	phone_number = request.POST.get('phone_number')
# 	e_mail = request.POST.get('e_mail')
# 	if id and name and phone_number:
# 		guess = Guess.objects.filter(phone_number=phone_number)
# 		if not guess.exists():
# 			event = Event.objects.filter(id=event_id)
# 			if event.exists():
# 				if Guess.objects.filter(event=event_id).count() < event.first().limit:
# 					print(1111)
# 					guess = Guess.objects.create(name=name, phone_number=phone_number, e_mail=e_mail)
# 					guess.event.add(event_id)
# 					result = {'error_code': 0, "data": {"event_id": str(event_id),
# 					                                   "guest_id": str(guess.id)}}
# 				else:
# 					result = {'error_code': 10006}
# 			else:
# 				result = {'error_code': 10004}
#
# 		else:
# 			result = {'error_code': 10005}
# 	else:
# 		result = {'error_code': 10001}
# 	return JsonResponse(result)


@require_http_methods(['POST'])
def add_guess(request):
	event_id = request.POST.get('id')
	name = request.POST.get('name')
	phone_number = request.POST.get('phone_number')
	e_mail = request.POST.get('e_mail')
	if event_id and name and phone_number:
		event = Event.objects.filter(id=event_id)
		if event.exists():
			if Guess.objects.filter(event=event_id).count() < event.first().limit:
				guess = Guess.objects.filter(phone_number=phone_number)
				print(guess, type(guess))  # <class 'django.db.models.query.QuerySet'>
				print(guess.first(), type(guess.first()))   # <class 'api.models.Guess'>
				if not guess.exists():
					print('ok')
					guess = Guess.objects.create(name=name, phone_number=phone_number,
					                             e_mail=e_mail)
					print(guess, type(guess))  # 这里Guess object (8) <class 'api.models.Guess'>
					guess.event.add(event_id)
					result = {'error_code': 0, "data": {"event_id": str(event_id),
				                                    "guest_id": str(guess.id)}}
				elif Guess.objects.filter(event=event_id):
					result = {'error_code': 100055}
				else:
					Guess.objects.get(phone_number=phone_number).event.add(event_id)
					result = {'error_code': 10005}
			else:
				result = {'error_code': 10006}
		else:
			result = {'error_code': 10004}
	else:
		result = {'error_code': 10001}
	return JsonResponse(result)
	

@require_http_methods(['POST'])
def get_event_guess(request):
	event_id = request.POST.get('id')
	phone_number = request.POST.get('phone_number')
	if event_id:
		try:
			event = Event.objects.get(id=event_id)
			if not phone_number:
				# 注意get和filter 的区分，get在没有查找到对象时会报错，filter会返回空列表
				guess_obj = Guess.objects.filter(event=event).values('id', 'name',
				                                                     'phone_number', 'e_mail')
				guess_list = []
				for i in guess_obj:
					guess_list.append(i)
				# print(guess_list)
				result = {'error_code': 0, "guest_list": guess_list}
			else:
				guess_obj = Guess.objects.filter(event=event, phone_number=phone_number).values('id', 'name',
				                                                                                'phone_number', 'e_mail')
				# print(guess_obj.first())
				if guess_obj:
					result = {'error_code': 0, "guest_list": guess_obj.first()}
				else:
					result = {'error_code': 10007}
		except:
			result = {'error_code': 10004}
	else:
		result = {'error_code': 10001}
	return JsonResponse(result)
	
	
@require_http_methods(['POST'])
def get_eventlist(request):
	title = request.POST.get('title')
	# print(title)
	event = Event.objects.filter(title__icontains=title)
	# print(event[0].status)
	if event:
		events = []
		# print(Event.objects.filter(title__icontains=title), len(event))
		for i in range(len(event)):
			events.append({"id": str(event[i].id), "title": event[i].title,
			               "status": str(event[i].status)})
		result = {"event_list": events, "error_code": 0}
	else:
		result = {"error_code": 10004}
	return JsonResponse(result)


@require_http_methods(['GET'])
def get_event_detail(request):
	event_id = request.GET.get('id')
	print(event_id)
	if event_id:
		event = Event.objects.filter(id=event_id)
		if event:
			event_detail = Event.objects.filter(id=event_id).values('id', 'title', 'status', 'limit',
			                                                        'address', 'times')
			result = {'error': 0, "event_detail": event_detail.first()}
		else:
			result = {'error': 10004}
	else:
		result = {'error': 10001}
	return JsonResponse(result)


@require_http_methods(['POST'])
def set_event_status(request):
	event_id = request.POST.get('id')
	event_status = request.POST.get('status')
	if event_id and event_status:
		event = Event.objects.filter(id=event_id)
		if event:
			if int(event_status) in [0, 1, 2]:
				try:
					Event.objects.filter(id=event_id).update(status=event_status)
					result = {'error': 0}
				except:
					result = {'msg': '数据更新失败'}
			else:
				result = {'error': 10003}
		else:
			result = {'error': 10004}
	else:
		result = {'error': 10001}
	return JsonResponse(result)


@require_http_methods(['POST'])
def register(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	if username and password:
		user = auth.authenticate(username=username, password=password)
		if user:
			token = Token.objects.filter(user=user).first().key
			# token = Token.objects.get(user=user).key    # 与上行代码等价
			uid = user.id
			result = {'error': 0, "token": token, "uid": str(uid)}
		else:
			result = {"error": 10000}
	else:
		result = {'error': 10001}
	return JsonResponse(result)


@require_http_methods(['POST'])
def sign(request):
	event_id = request.POST.get('id')
	phone_number = request.POST.get('phone_number')
	if event_id and phone_number:
		event = Event.objects.filter(id=event_id)
		guess = Guess.objects.filter(phone_number=phone_number)
		if event and guess:
			event_obj = Event.objects.filter(guess__phone_number=phone_number, id=event_id)
			if event_obj:
				if event_obj.first().status !=2:
					cursor = connection.cursor()
					cursor.execute('select sign from api_guess_event a where a.guess_id=%s AND a.event_id= %s', [
						guess.first().id, event.first().id
					])
					# print(cursor.fetchone())
					if (cursor.fetchone())[0] == 0:
						cursor.execute('update api_guess_event a set a.sign =1 WHERE a.guess_id=%s AND a.event_id= %s',[
							guess.first().id, event.first().id
						])
						result = {'error': 0}
					else:
						result = {'error': 10009}
					
				else:
					result = {'error': 10010}
			else:
				result = {'error': 10008}
		else:
			result = {'msg': '会议或参会人员不存在！'}
	else:
		result = {'error': 10001}
	return JsonResponse(result)