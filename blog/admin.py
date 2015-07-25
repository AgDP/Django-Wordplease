from blog.models import Blog
from django.contrib import admin

class BlogAdmin(admin.ModelAdmin):
    pass

admin.site.register(Blog, BlogAdmin)