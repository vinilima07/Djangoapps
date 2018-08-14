from django.shortcuts import render

# Create your views here.
def head(request):
    return render(request, 'readhistory/head.html')

def home(request):
    return render(request, 'readhistory/home.html')
