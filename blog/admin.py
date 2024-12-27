from django.contrib import admin
from .models import Post
from django.utils.html import format_html

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','content_preview', 'country', 'image_preview', 'created_at', 'updated_at']
    

    def content_preview(self, obj):
        words = obj.content.split()
        preview = ' '.join(words[:3]) 
        if len(words) > 3:
            preview += '...'
        return preview

    content_preview.short_description = 'Content Preview'  

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="75" height="75" />', obj.image.url)
        return "No Image"

    image_preview.short_description = 'Image Preview'
