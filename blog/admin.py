from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import BlogPost
from django.utils.html import format_html


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    # Use the thumbnail and link display methods
    list_display = ['title', 'created_at', 'image_thumbnail', 'link_display']
    list_display_links = ['title']  # Make the title a link to the edit page
    search_fields = ['title']
    summernote_fields = ('body',)  # Use Summernote editor for the body field

    # Customize the list view to display the image thumbnail
    def image_thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" alt="{}" width="50" height="50">', obj.image.url, obj.title)
        return 'No Image'
    image_thumbnail.short_description = 'Image'  # Column header

    readonly_fields = ['image_thumbnail']  # Make the image thumbnail read-only

    # Display the link field in the list view
    def link_display(self, obj):
        return obj.link if obj.link else 'No Link'
    link_display.short_description = 'Link'
