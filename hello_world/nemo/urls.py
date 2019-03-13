# -*- coding: utf-8 -*-#
# __author__ = 'Bo_lin Chen'
# Date: 2019/3/13


from django.urls import path
from nemo import views

urlpatterns = [
    path('login/', views.nemo_login),
    path('is_login/', views.nemo_is_login),
    path('test/', views.nemo_test)
]


