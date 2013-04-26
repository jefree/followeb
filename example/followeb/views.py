# Create your views here.

from django.http import HttpResponse,HttpResponseBadRequest
from django.shortcuts import render, redirect
from models import Resource, ResourceVersion

import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import os

def addSubscriptionView(request):
	
	if request.method == 'POST':
		
		url =  request.POST['url']
		title = request.POST['title']
		description = request.POST['description']

		os.makedirs('./followeb/static/followeb/file_history/'+title)
		file_name = './followeb/static/followeb/file_history/'+title+'/version_1.html' 

		res_file = open(file_name, 'w')
		res_file.write(requests.get(url).text.encode("UTF-8"))
		res_file.close()

		resource = Resource(url=url, title=title, description=description)
		resource.save()

		version = ResourceVersion(resource=resource, version=1, date=datetime.now(), resource_file=file_name)
		version.save()

		return redirect('/followeb/')

	return HttpResponseBadRequest('Bad Request')
	

def getPreviewView(request, url):
	
	if not request.is_ajax():
		return HttpResponseBadRequest('Bad Request')

	info = {'error':False,
			'title':'',
			'description':'',
			'image':''}

	try:
		
		request = requests.get(url)

		if request:

			html = BeautifulSoup(request.text)

			#get title
			info['title'] = html.find('title').text
			
			#get description
			meta = html.find(attrs={"name":"description"})

			if meta:
				info['description'] = meta['content']

			#get image
			img_tags = html.findAll("meta", property='og:image')
			key_src = 'content'

			if not img_tags:
				img_tags = html.findAll("img")
				key_src='src'

			if img_tags:

				for img in img_tags:

					src = img[key_src]

					if src.count('gif') == 0:

						if src[:2] == '..':
							info['image'] = url + src
						else:
							info['image'] = src

						break
						
	except Exception as e:

		#print 'Exception:', e

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
	
	
