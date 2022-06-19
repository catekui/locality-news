from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from PIL import Image
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)

    def save_loc(self):
        self.save()

    def __str__(self):
        return self.name
    
