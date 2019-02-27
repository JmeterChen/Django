from django.test import TestCase
from django import template
from django.shortcuts import render
# Create your tests here.

from django.conf import settings

import csv

a = 'kobe'
b = '112233'

def home():
	with open('.//..//user.csv','r',encoding='utf-8') as f:
		reader = csv.reader(f)
		for i in reader:
			# if username == 'admin' and password == '123456':
			
			if a == i[0] and b == i[1]:
				print(i)
				return 'ok'
		else:
			return 'no'

# print(home())

settings.configure()
t = template.Template('My name is {{ name }}!')
c = template.Context({'name':'Chenbolin'})
print(t.render(c))
