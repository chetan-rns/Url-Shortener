from django.db import models
from .utils import *
# Create your models here.


class urlData(models.Model):
	url=models.CharField(max_length=220,)
	shortcode=models.CharField(max_length=15,unique=True,blank=True)
	update=models.DateTimeField(auto_now=True)
	timestamp=models.DateTimeField(auto_now_add=True)

	def save(self,*args,**kwargs):
		if(self.shortcode is None or self.shortcode==''):
			self.shortcode=createShortCode(self)
		super(urlData,self).save(*args,**kwargs)

	def __str__(self):	
		return str(self.url)