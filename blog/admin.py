from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'image', 'link']  # Add image and link to the list display
    list_display_links = ['title']  # Make the title a link to the edit page
    search_fields = ['title']

    # Customize the list view to display the image thumbnail
    def image_thumbnail(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" alt="{obj.title}" width="50" height="50">'
        return 'No Image'
    image_thumbnail.short_description = 'Image'  # Column header

    readonly_fields = ['image_thumbnail']  # Make the image thumbnail read-only

    # You can also add the link field to the list view if desired
    def link_display(self, obj):
        return obj.link if obj.link else 'No Link'
    link_display.short_description = 'Link'
