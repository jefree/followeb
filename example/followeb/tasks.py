#module for some tasks
from datetime import timedelta,datetime
from celery.task import periodic_task
import requests
from bs4 import BeautifulSoup

import os
import hashlib
from models import *


def genPreview(url):

	info = {'error':False}

	try:
		request = requests.get(url)

		if request:

			html = BeautifulSoup(request.text)
			info['url'] = request.url

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

	except:
		info['error'] = True

	return info

"""
@param: resource
@param: code_html
@param: version
This function create new version for resource specified
"""
def create_new_version(resource, code_html,version):

	title = resource.title

	if not os.path.exists('followeb/static/followeb/history_file/'+title):
		#create new folder
		os.makedirs('followeb/static/followeb/history_file/'+title)

	file_name = 'followeb/static/followeb/history_file/'+title+'/version_'+str(version)+'.html' 

	#create new file
	res_file = open(file_name, 'w')
	res_file.write(code_html.encode("UTF-8"))
	res_file.close()

	version = ResourceVersion(resource=resource, version=version, date=datetime.now(), resource_file=file_name)
	version.save()

"""
This function check the changes for each suscription  
"""
@periodic_task(run_every=timedelta(seconds=10))
def update_resource():

	resources = Resource.objects.all()

	for res in resources:

		html_tmp = requests.get(res.url).text

		last_version = res.resourceversion_set.all().order_by('-version')[0]

		html_old = last_version.resource_file.read()

		# compare html_tmp and html_old with md5 checksum

		md5_tmp = hashlib.md5(html_tmp.encode("UTF-8")).digest()
		md5_old = hashlib.md5(html_old).digest()

		if not md5_tmp == md5_old:	#was a change in the website
			create_new_version(res,html_tmp,last_version.version+1) 
			print "change"+res.title
		else:
			print "not change"+res.title

