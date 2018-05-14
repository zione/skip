from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Poster(models.Model):
    title = models.CharField(max_length=64)
    desc = models.TextField()
    url = models.CharField(max_length=256)
    mode = models.IntegerField()
    imgurl = models.CharField(max_length=256)
    createTime = models.DateTimeField(auto_now_add=True)
    publishTime = models.DateTimeField()
    modifyTime = models.DateTimeField(auto_now=True)