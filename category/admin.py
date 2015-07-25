from category.models import Category
from django.contrib import admin
from post.models import Post


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name',)
    search_fields = ('name',)

    fieldsets = (
        ('Name', {
            'fields': ('name',),
            'classes': ('wide',)
        }),
    )

admin.site.register(Category, CategoryAdmin)