# -*- coding: utf-8 -*-#
# __author__ = 'Bo_lin Chen'
# Date: 2019/3/14

from django.urls import path
from wood import views


urlpatterns = [
    path('login/', views.login),
	path('demo_db/', views.db_test)
]
