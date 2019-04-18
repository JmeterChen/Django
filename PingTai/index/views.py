from django.shortcuts import render
from index.models import *
# Create your views here.


def index(request):
    students = Student.objects.all()
    # print(students)
    return render(request, 'index.html', {'student': students, 'flag': 0})
