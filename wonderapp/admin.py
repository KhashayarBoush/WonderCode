from django.contrib import admin
from . import models

@admin.register(models.User)
class AdminUser(admin.ModelAdmin):
    pass
