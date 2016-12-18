from __future__ import unicode_literals
from django.contrib.auth.models import User


from django.db import models

class Blog(models.Model):
	title=models.CharField(max_length=200)
	content=models.TextField()
	date=models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, default=User.objects.get(pk=1).pk)

# Create your models here.
