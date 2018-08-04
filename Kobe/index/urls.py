# coding=utf-8
# @Author:ChenBo lin


from django.conf.urls import include, url
from django.contrib import admin
from index import views

urlpatterns = [
    url(r'^home/$', 'index.views.home'),
    url(r'^login/$', 'index.views.login'),
    url(r'^sign/$', 'index.views.sign'),
    url(r'^api_sign/$', 'index.views.api_sign'),
    url(r'^api_login/$', 'index.views.api_login'),
    url(r'^bugs/', 'index.views.bugs'),
    url(r'^bugs_tch/', 'index.views.bugs_teach'),
    url(r'^weather/', 'index.views.weather')
]
