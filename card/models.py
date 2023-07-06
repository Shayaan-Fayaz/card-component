from django.db import models

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=200)
    roles = models.CharField(max_length=200)
    img = models.URLField()
    github_link = models.URLField()
