from django.conf.urls import patterns, url

from followeb import views

urlpatterns = patterns('',

	url(r'^$', views.index, name='index'),
	url(r'^add/$', views.add, name='add'),
	url(r'^details/$', views.details, name='details'),
)
	
