from django.db import models

# Create your models here.

class Resource(models.Model):
	
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=300, blank=True)
	url = models.URLField(editable=False)
	
	def __unicode__(self):
		return self.title

class ResourceVersion(models.Model):
	
	resource = models.ForeignKey(Resource)
	version = models.IntegerField(editable=False)
	date = models.DateTimeField(blank=True, editable=False)
	resource_file = models.FileField(upload_to='./file_history/', editable=False)
	
	def __unicode__(self):
		return self.resource.title+'_'+str(self.version) 
