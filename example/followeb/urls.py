from django.conf.urls import patterns, url

from followeb import views

urlpatterns = patterns('',

	url(r'^$', views.index, name='index'))
	
