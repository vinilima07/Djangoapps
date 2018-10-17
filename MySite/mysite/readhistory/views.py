from django.shortcuts import render
from django.db import models

# Create your views here.
def head(request):
    return render(request, 'readhistory/head.html')

def home(request):
    return render(request, 'readhistory/home.html')

def login(request):
    return render(request, 'readhistory/login.html')

def write(request):
    return render(request, 'readhistory/write.html')

def read(request):
    return render(request, 'readhistory/read.html')

def myhistory(request):
    return render(request, 'readhistory/myhistory.html')

def test(request):
	return render(request, 'readhistory/test.html', 
		{'content':['If you wanna call me', '(31)93242398'],
		'myname':testando()})

def testando():
	return 'color'