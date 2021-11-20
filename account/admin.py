from django.contrib import admin

from account.models import UserProfile


@admin.register(UserProfile)
class AccountAdmin(admin.ModelAdmin):
    pass
