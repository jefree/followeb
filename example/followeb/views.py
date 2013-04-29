# Create your views here.

from django.http import HttpResponse,HttpResponseBadRequest
from django.shortcuts import render, redirect
from models import Resource, ResourceVersion

import json
import requests
from datetime import datetime
import os
import tasks

def addSubscriptionView(request):
	
	if request.method == 'POST':
		
		url =  request.POST['url']
		title = request.POST['title']
		description = request.POST['description']

		os.makedirs('followeb/static/followeb/file_history/'+title)
		file_name = 'followeb/static/followeb/file_history/'+title+'/version_1.html' 

		html_request = requests.get(url)

		res_file = open(file_name, 'w')
		res_file.write(html_request.text.encode("UTF-8"))
		res_file.close()

		resource = Resource(url=html_request.url, title=title, description=description)
		resource.save()

		version = ResourceVersion(resource=resource, version=1, date=datetime.now(), resource_file=file_name)
		version.save()

		return redirect('/followeb/')

	return HttpResponseBadRequest('Bad Request')

def performTaskView(request, url='', title=''):

    if not request.is_ajax():
        return HttpResponseBadRequest('Bad Request')

    info = dict()

    if not url == '' :   #get preview

        preview = tasks.genPreview(url)
        info.update(preview)

        #validate that not exists another subscription with same url
        if len( Resource.objects.filter(url=info['url']) ) != 0:
            info['error'] = True
            info['error-message'] = 'This Subscription already exists.'
    	
            
    elif not title == '':  #check repeated title

        if len(Resource.objects.filter(title=title)) > 0:
            info['error'] = True

    return HttpResponse('('+json.dumps(info)+')')

def index(request):
	context = {'image':'index.png', 'title':'INDEX VIEW'}
	return render(request,  'followeb/image-template.html', context)
	
def add(request):
	context = {'image':'add.png', 'title':'ADD VIEW'}
	return render(request,  'followeb/add.html', context)

def details(request):
	context = {'image':'details.png', 'title':'DETAILS VIEW'}
	return render(request,  'followeb/image-template.html', context)
	
	
