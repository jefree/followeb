#module for some tasks

import requests
from bs4 import BeautifulSoup

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