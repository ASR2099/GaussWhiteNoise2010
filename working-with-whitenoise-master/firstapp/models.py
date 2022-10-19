from django.db import models
import datetime

# Create your models here.
class Post(models.Model):
    userId  = models.TextField(default = 1)
    title = models.CharField("default Title",max_length = 200)
    body = models.TextField(default = 'Body of post goes here')
    picture = models.ImageField(default ='default.png')

