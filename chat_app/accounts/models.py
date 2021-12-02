from django.db import models
from django.contrib.auth.models import User
from django.db.models import OneToOneField
from django.db.models.fields import CharField
# Create your models here.

class UserProfile(models.Model):
    profile = OneToOneField(User, null=True, on_delete=models.SET_NULL)