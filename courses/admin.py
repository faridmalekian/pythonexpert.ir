from django.contrib import admin

import csv
import datetime

from django.http import HttpResponse
from courses.models import Course, Module, Comment


class ModuleInline(admin.StackedInline):
    model = Module


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title','owner','slug' ,'created']
    list_filter = ['created']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('owner', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('owner',  'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

