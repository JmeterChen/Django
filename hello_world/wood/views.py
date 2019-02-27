from django.shortcuts import render
from django.http import HttpResponse, Http404 
from django.http import JsonResponse

# Create your views here.

def home(request):
	return render(request, 'current_datetime.html')