# Create your views here.

from django.shortcuts import render

def index(request):
	
	context = {'image':'add.png', 'title':'INDEX VIEW'}
	
	return render(request,  'followeb/image-template.html', context,)
	
	
	
