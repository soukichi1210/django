# myapp/models.py

from django.db import models
from django.contrib.auth.models import User

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

# myapp/models.py
from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=15)
    gender = models.IntegerField(choices=[(0, 'Male'), (1, 'Female')])
    student_id = models.IntegerField(unique=True)
    password = models.CharField(max_length=15)
    age = models.IntegerField()
    profile = models.TextField(max_length=200)
    image_url = models.URLField(blank=True, null=True)

