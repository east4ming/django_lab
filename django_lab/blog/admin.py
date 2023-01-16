from django.contrib import admin

from django_lab.blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass
