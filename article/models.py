from django.db import models

# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=50)
	description = models.CharField(max_length=255)
	content = models.TextField()
	dateline = models.DateTimeField(auto_now=True)

