from django.db import models

# Create your models here.

class urlData(models.Model):
	url=models.CharField(max_length=220,)

	def __str__(self):	
		return str(self.url)