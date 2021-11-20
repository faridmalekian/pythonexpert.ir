from django.db import models


class Consulting(models.Model):

    name = models.CharField(max_length=200)
    email = models.EmailField()
    tel = models.CharField(max_length=11,unique=True)
    add = models.TextField(null=True)
    consulting = models.BooleanField(default=False)