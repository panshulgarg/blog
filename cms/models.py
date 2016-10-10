from __future__ import unicode_literals

from django.db import models

class Blog(models.Model):
	title=models.CharField(max_length=200)
	content=models.TextField()
	date=models.DateTimeField(auto_now_add=True)

# Create your models here.
