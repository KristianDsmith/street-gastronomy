from django.db import models
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    # This field now uses django-summernote for rich text editing
    body = SummernoteTextField()
    image = models.ImageField(upload_to='blog_images/',
                              blank=True, null=True)  # Field for images
    link = models.URLField(blank=True, null=True)  # Field for links
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
