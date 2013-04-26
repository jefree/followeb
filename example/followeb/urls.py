from django.conf.urls import patterns, url

from followeb import views

urlpatterns = patterns('',

	url(r'^$', views.index, name='index'),
	url(r'^add/$', views.add, name='add'),
	url(r'^details/$', views.details, name='details'),
	url(r'^tasks/preview/(?P<url>.+)/$', views.getPreviewView, name='preview'),
	url(r'^add/subscribe/', views.addSubscriptionView, name='subscribe'),
)
	
