from django.db import models
import os

from django.contrib.auth.models import User

from courses_category.models import Category


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name , ext = os.path.splitext(base_name)
    return name,ext

def upload_image_path(instance,filename):
    name , ext = get_filename_ext(filename)
    final_name = f"{instance.user.id}-{instance.user.username}{ext}"
    return f'avatar/{final_name}'

class UserProfile(models.Model):
    user   = models.ForeignKey(User,on_delete=models.CASCADE)
    your_expertise = models.ManyToManyField(Category)
    about_you = models.TextField(null=True)
    avatar = models.ImageField(upload_to=upload_image_path)

