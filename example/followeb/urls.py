from django.conf.urls import patterns, url

from followeb import views

urlpatterns = patterns('',

	url(r'^$', views.index, name='index'),
	url(r'^add/$', views.add, name='add'),
	url(r'^history/(?P<res_id>\d+)/$', views.history, name='history'),

	url(r'^tasks/checktitle/(?P<title>[a-zA-Z]+)/$', views.performTaskView, name='checktitle'),
	url(r'^tasks/preview/(?P<url>.+)/$', views.performTaskView, name='preview'),
	url(r'^add/subscribe/', views.addSubscriptionView, name='subscribe'),
)
	
