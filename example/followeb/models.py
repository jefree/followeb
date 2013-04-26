from django.db import models

# Create your models here.

class Resource(models.Model):
	
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=300, blank=True)
	url = models.URLField()
	
	def __unicode__(self):
		return self.title

class ResourceVersion(models.Model):		
	
	resource = models.ForeignKey(Resource)
	version = models.IntegerField()
	date = models.DateTimeField()
	resource_file = models.FileField(upload_to='./file_history/')
	
	def __unicode__(self):
		return self.resource.title+'_'+str(self.version) 
