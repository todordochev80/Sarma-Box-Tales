from django.contrib import admin
from .models import Story, Tag


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'content')


admin.site.register(Tag)

