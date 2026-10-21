
# Register your models here.

from django.contrib import admin

from .models import PostModel


@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at',)