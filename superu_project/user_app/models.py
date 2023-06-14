from django.db import models
from django.utils.html import mark_safe

# Create your models here.

class user_profile(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    bio = models.TextField(max_length=255)
    profile_picture = models.ImageField(upload_to='profile_pictures/',verbose_name='User_profile_pic')







