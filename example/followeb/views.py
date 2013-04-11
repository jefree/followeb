# Create your views here.

from django.shortcuts import render

def index(request):
	
	context = {'image':'index.png', 'title':'INDEX VIEW'}
	return render(request,  'followeb/image-template.html', context)
	
def add(request):
	
	context = {'image':'add.png', 'title':'ADD VIEW'}
	return render(request,  'followeb/add.html', context)

def details(request):
	
	context = {'image':'details.png', 'title':'DETAILS VIEW'}
	return render(request,  'followeb/image-template.html', context)
	
	
