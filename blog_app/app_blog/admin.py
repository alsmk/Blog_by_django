from django.contrib import admin

# Register your models here.
from app_blog.models import Blog, Comment, Like


admin.site.register(Blog)
admin.site.register(Like)
admin.site.register(Comment)