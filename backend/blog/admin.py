from django.contrib import admin
from blog.models import BlogCategory, BlogPost, Comment

# Register your models here.
admin.site.register(BlogCategory)
admin.site.register(BlogPost)
admin.site.register(Comment)