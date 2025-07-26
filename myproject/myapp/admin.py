# myapp/admin.py

from django.contrib import admin
from .models import UserProfile, MyModel

admin.site.register(UserProfile)
admin.site.register(MyModel)
