from django.contrib import admin
from . import models


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'owner']
    list_display_links = ['name']
    list_filter = ['owner']
    

class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_done', 'deadline', 'project', 'owner', 'created_at']
    list_filter = ['is_done', 'project', 'owner', 'deadline', 'created_at']

admin.site.register(models.Project)
admin.site.register(models.Task)