from django.shortcuts import render
from django.http import HttpResponse
from nemo.models import User

# Create your views here.


def nemo_charge(request):
	return HttpResponse('This is nemo home!')


def nemo_test(request):
	a = User.objects.all()[0]
	return HttpResponse(a.username)



def nemo_login(request):
	cookie_username = request.COOKIES.get('username')
	cookie_password = request.get_signed_cookie('pwd', default=None)
	users = User.objects.filter(username=cookie_username, password=cookie_password)
	if users:
		return render(request, 'nemo_home.html', {'users_name': cookie_username})
	else:
		return render(request, 'nemo_login.html')


def nemo_is_login(request):
	input_username = request.POST.get('username')
	input_password = request.POST.get('password')
	is_save = request.POST.get('is_save')
	print(is_save, input_username, input_password)
	if input_username and input_password:
		users = User.objects.filter(username=input_username, password=input_password)
		print(users)
		if users:
			res = render(request, 'nemo_home.html', {'users_name': input_username})
			if is_save =='on':
				res.set_cookie(key='user_name', value=input_username)
				res.set_cookie(key='pass_word', value=input_password)
			return res
		else:
			return render(request, 'error.html', {'msg': '用户名或密码错误哦'})
	else:
		return render(request, 'error.html', {'msg': '请确认用户名和密码已填写'})

