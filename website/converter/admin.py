from django.contrib import admin

from .models import Video


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_file')
    search_fields = ('title',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'created_at', 'text', 'is_published')
    list_editable = ('is_published',)
    list_filter = ('created_at',)


admin.site.register(Video, VideoAdmin)
