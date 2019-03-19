from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.http import require_http_methods
from api.models import *
import time
# Create your views here.


@require_http_methods(['POST'])
def add_guest(request):
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
						time.strptime(times,'%Y-%m-%d %H-%M-%S')
					except:
						result = {'msg': '时间格式错误'}
					else:
						try:
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
					result = {'error': 10003}
				
			except:
				result = {'msg': 'limit或者status字段不是纯数字'}
			
		else:
			result = {'error': 10002}
		
	else:
		result = {'error': 10001}
	
	return JsonResponse(result)
