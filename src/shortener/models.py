from django.db import models
from .utils import *
from django.conf import settings
# Create your models here.

class urlDataManager(models.Manager):
	def refresh_shortcodes(self):
		qs=urlData.objects.filter(id__gte=1)
		new_codes=0
		for q in qs:
			q.shortcode=createShortCode(q)
			print(q.shortcode)
			q.save()
			new_codes+=1

		return "New codes made:{i}".format(i=new_codes)

class urlData(models.Model):
	url=models.CharField(max_length=220,)
	shortcode=models.CharField(max_length=15,unique=True,blank=True)
	update=models.DateTimeField(auto_now=True)
	timestamp=models.DateTimeField(auto_now_add=True)
	active=models.BooleanField(default=True)

	objects=urlDataManager()
	def save(self,*args,**kwargs):
		if(self.shortcode is None or self.shortcode==''):
			self.shortcode=createShortCode(self)
		super(urlData,self).save(*args,**kwargs)

	def __str__(self):	
		return str(self.url)