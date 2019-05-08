from django.shortcuts import render
from index.models import *

# Create your views here.


def index(request):
	students = Student.objects.all()
	return render(request, 'index.html', {'students': students})