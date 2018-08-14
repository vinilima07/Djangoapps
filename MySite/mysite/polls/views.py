from django.shortcuts import render
# Create your views here.

def index(request):
	return render(request, 'polls/index.html')

def contactUs(request):
	return HttpResponse("<br/><br/><p>(31)997368875</p><br/><br/>")