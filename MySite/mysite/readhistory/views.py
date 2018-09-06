from django.shortcuts import render

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
