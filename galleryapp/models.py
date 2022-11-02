from email.policy import default
from operator import mod
from random import choices
from secrets import choice
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Slider(models.Model):
    image = models.ImageField(upload_to = "Slider/")


class Gallery(models.Model):

    name = models.CharField( max_length=100)
    image = models.FileField(upload_to = "Gallery/")
    description = models.TextField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)