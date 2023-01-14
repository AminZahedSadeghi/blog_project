from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'post_time_modified']
    ordering = ['post_time_modified']


admin.site.register(Post, PostAdmin)
