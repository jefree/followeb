# Create your views here.

from followeb.models import *
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
	context['lista']=Resource.objects.all()
	return render(request,  'followeb/index.html', context)
	
def add(request):
	
	context = {'image':'add.png', 'title':'ADD VIEW'}
	return render(request,  'followeb/add.html', context)

"""
@return: This function return a web site with the information of the consultation
"""
def history(request,res_id):
	context = {}
	#Get the version list for this resource
	context['list_history']=Resource.objects.get(id=res_id).resourceversion_set.all()
	return render(request,  'followeb/history.html', context)
