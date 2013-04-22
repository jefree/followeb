# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

import requests
import bs4
import json
import os

def getPreviewView(request, url):
	
	info = {'error':False,
			'title':'',
			'description':'',
			'image':''}

	try:
		
		request = requests.get(url)

		if request:

			html = bs4.BeautifulSoup(request.text)

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
	
	
