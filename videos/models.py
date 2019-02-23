from django.db import models

class Video(models.Model):
	summary = models.CharField(max_length=200)
	url = models.TextField()
	
	
	def __str__(self):
		return self.summary
