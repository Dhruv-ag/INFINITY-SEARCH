from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title=models.CharField(max_length=100)
    type=models.CharField(max_length=50)
    cast=models.TextField()
    
