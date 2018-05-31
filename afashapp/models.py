from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    title = models.CharField()
    text = models.CharField()
    date = models.DateTimeField(auto_now=True)
    
