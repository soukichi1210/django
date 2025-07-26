# myapp/models.py

from django.db import models
from django.contrib.auth.models import User

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    hobby = models.CharField(max_length=100, blank=True)
    skills = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
