# encoding=utf-8

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
import json
from django.contrib import auth
from models import *


# Create your views here.


# def home(request):
#     print(request.method)
#     name = request.GET.get('name')
#     return render(request, 'nba.html', {'name': name})
#
# def menu(request):
#     return render(request, 'players.html')
#
#
# def demo(request):
#     return HttpResponse


def home(request):

    # username = request.COOKIES.get('username')
    username = request.session.get('username')
    if username:
        return render(request, 'home_login.html')
    else:
        return HttpResponseRedirect('/index/login')

    # if request.method == 'POST':
    #     username = request.GET.get('username')
    #     password = request.GET.get('password')
    #     print(request.COOKIES.get())
    #     if username and password:
    #         info = u'欢迎登录，%s'% username
    #
    #     else:
    #         info = u'账号或者密码不能为空！'
    #         return HttpResponse(status=400, content_type='application/json', content=json.dumps(info, ensure_ascii=False))
    # else:
    #     info = u'请求类型无效'
    #
    # data = {"info": info}
    #
    # return HttpResponse(content_type='application/json', content=json.dumps(data, ensure_ascii=False))
    # # return render(request, 'home.html', {'info': info})
    #
    # # return HttpResponse('123')
    # return render(request, 'home_login.html')


def login(request):
    return render(request, 'login.html')


def sign(request):
    return render(request, 'sign.html')

def api_sign(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username and password:
        user = User.objects.filter(name=username)
        if not user.exists():
            try:
                # print(User.objects.create(name=username, pwd=password))
                # print(User(name=username, pwd=password).save())
                # # # user = User(name='tianlaoshi')
                # # # user.pwd = '0000'
                # # # user.save()
                # # user = User.objects.filter(name='tianlaoshi').first()
                # # user.pwd = '0000'
                # # user.save()
                # user = User.objects.filter(name='tianlaoshi').update(pwd='0000')
                User.objects.filter(name='tianlaoshi').delete()
                return HttpResponseRedirect('/index/login/')
            except:
                return render(request, 'error.html', {'info': u'未知错误'})
        else:
            return render(request, 'error.html', {'info': u'用户已存在'})
    else:
        return render(request, 'error.html', {'info': u'缺少必填参数'})

def api_login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    isSave = request.POST.get("isSave")
    # print username, password, isSave
    # user = auth.authenticate(username=username, password=password)
    # user = User.objects.get(name=username, pwd=password)
    user = User.objects.filter(name=username, pwd=password)
    print(type(user))
    # if username == 'admin' and password == 'admin':
    if user:
        if isSave == 'on':
            res = render(request, 'home_login.html', {'username': username})
            request.session['username'] = username
            # res.set_cookie('username', username)
            return res
        else:
            return render(request, 'home_login.html', {'username': username})
        # return render(request, 'home.html', {'username': username})

    else:
        return render(request, 'login.html')


# my_method
def bugs(request):

    month = request.GET.get('month')
    data = {
            "business_autoFans_J": [{"2016_08": 14},  {"2016_09": 15}, {"2016_10": 9}],
            "autoAX": [{"2016_08": 7},  {"2016_09": 32}, {"2016_10": 0}],
            "autoAX_admin": [{"2016_08": 5},  {"2016_09": 13}, {"2016_10": 2}],
    }

    list_data = []
    for i in data:
        for m in data[i]:
            list_data.append(m)

    sum_data = 0
    for x in list_data:
        for y in x:
            if y[-2:] == month:
                sum_data += x[y]

    return render(request, 'bugs.html', {'month': month, 'sum_data': sum_data})



# teach_method
def bugs_teach(request):
    result = {}
    data = {
        "business_autoFans_J": [{"2016_08": 14}, {"2016_09": 15}, {"2016_10": 9}],
        "autoAX": [{"2016_08": 7}, {"2016_09": 32}, {"2016_10": 0}],
        "autoAX_admin": [{"2016_08": 5}, {"2016_09": 13}, {"2016_10": 2}],
    }
    if request.method == 'POST':
        # month = request.GET.get("month")
        month = 0
        month = json.loads(request.body).get("month")
        if month:
            try:
                month = int(month)
            except:
                info = u"month不是纯数字"
            else:
                if month in range(1, 13):
                    total = 0
                    for v in data.values():
                        for i in v:
                           for m, bug in i.items():
                               if int(m.split('_')[1]) == month:
                                   total += bug
                    # info= u'%d月共有bug%d个' % (month, total)
                    code = 0
                    result['data'] = {'month': month, "total": total}

                else:
                    info = u'month是无效月份'
                    code = 1
        else:
            info = u'缺少必填参数month'
            code = 2
    else:
        info = u'请求类型不合理'
        code = 3

    # return render(request, 'home.html', {'info': info})
    result['msg'] = info
    result['code'] = code

    return HttpResponse(content_type='application/json', content=json.dumps(result, ensure_ascii=False))


def weather(request):
    result = {}
    if request.method == 'POST':
        body = request.body

        try:
            dic = json.loads(body)
        except:
            result['error_code'] = 10003

        else:
            theCityCode = dic.get('theCityCode')

        # theCityCode = json.loads(request.body).get('theCityCode')

            if theCityCode:
                theCityCode = int(theCityCode)

                if theCityCode == 1:
                    result['error_code'] = 0
                    result['cid'] = "1"
                    result['name'] = u'北京市'
                    result['weather_info'] = u'今日天气实况：气温：19℃；风向/风力：东北风 1级；湿度：54%'

                else:
                    result['error_code'] = 10002

            else:
                result['error_code'] = 10001

    else:
        result['error_code'] = 10003

    return HttpResponse(content_type='application/json', content=json.dumps(result, ensure_ascii=False))

