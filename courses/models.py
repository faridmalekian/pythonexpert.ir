from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db import models
import os
from django.db.models import Avg, Q
import account.models
from courses_category.models import Category


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f'courses/{final_name}'


class CourseManager(models.Manager):
    def get_active_couses(self):
        return self.get_queryset().filter(active=True)

    def get_courses_by_category(self, category_name):
        return self.get_queryset().filter(category__slug__iexact=category_name)

    def get_by_id(self, course_id):
        qs = self.get_queryset().filter(id=course_id)

        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def search(self, query):
        lookup = Q(title__icontains=query) | Q(overview__icontains=query) | Q(tag__title__icontains=query)
        return self.get_queryset().filter(lookup, active=True, ).distinct()


class Course(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='courses_created', on_delete=models.CASCADE,
                              verbose_name='مدرس')
    title = models.CharField(max_length=200)
    price = models.IntegerField(null=True)
    image = models.ImageField(upload_to=upload_image_path, null=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='courses_joined', blank=True)
    category = models.ManyToManyField(Category)
    active = models.BooleanField(default=False, null=True)
    time = models.TextField(null=True)

    objects = CourseManager()

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'دوره ها'
        verbose_name = 'دوره'

    def get_absolute_url(self):
        return f"/course/{self.id}/{self.slug}"

    def __str__(self):
        return self.title


class Module(models.Model):
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    duration = models.TextField(null=True)


class Comment(models.Model):
    post = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    reply = models.TextField(blank=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.owner)

    def get_url_image_owner(self):
        return account.models.UserProfile.objects.get_queryset().filter(user_id=self.owner_id).first()
