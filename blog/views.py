from django.shortcuts import render
from blog.models import BlogPost


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'index.html')


def blog(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'blog.html', {'blog_posts': blog_posts})

def english(request):
    return render(request, 'index.html')

def swedish(request):
    return render(request, 'swedish.html')

def german(request):
    return render(request, 'german.html')
