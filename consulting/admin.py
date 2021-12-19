from django.contrib import admin
from .models import Consulting


@admin.register(Consulting)
class ConsultingAdmin(admin.ModelAdmin):
    list_display = ['name', 'tel']
    list_filter = ['consulting']
    search_fields = ['consulting', 'tel']
