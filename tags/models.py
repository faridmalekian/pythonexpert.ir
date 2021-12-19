from django.db import models

from courses.models import Course


class Tag(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    active = models.BooleanField(default=True)
    courses = models.ManyToManyField(Course, blank=True)

    def __str__(self):
        return self.title
