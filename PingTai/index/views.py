from django.shortcuts import render
from index.models import *
# Create your views here.


def index(request):
	students = Student.objects.all()
	# print(students)
	return render(request, 'index.html', {'student': students, 'flag': 0})


def demo(request):
	return render(request, 'demo_huice.html')


def login(request):
	return render(request, 'login.html')


def register(request):
	return render(request, 'register.html')