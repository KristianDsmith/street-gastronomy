from django.shortcuts import render
from blog.models import BlogPost

def home(request):
    return render(request, 'en/index_en.html')

def about(request):
    # Assuming the site's default language is English
    return render(request, 'en/index_en.html')

def blog(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'blog.html', {'blog_posts': blog_posts})

def index(request):
    return render(request, 'en/index_en.html')

def swedish(request):
    return render(request, 'se/index_se.html')

def german(request):
    return render(request, 'de/index_de.html')

def about_se(request):
    return render(request, 'se/index_se.html')

def about_de(request):
    return render(request, 'de/index_de.html')

