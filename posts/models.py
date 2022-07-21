from django.db import models

class Post(models.Model):
    userId = models.IntegerField()
    title = models.CharField(max_length=200)
    body = models.TextField()

