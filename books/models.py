from django.db import models

class Book(models.Model):
	image = models.ImageField(upload_to="images/")
	summary = models.CharField(max_length=200)
	url = models.TextField()
	
	
	def __str__(self):
		return self.summary
