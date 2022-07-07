from django.shortcuts import render, redirect
from .models import Article, Topik


def beranda(request):
    blogs = Article.objects.all()
    context = {
        'title': 'Beranda | Bappeda Kab. Jayapura',
        'blog': blogs
    }

    return render(request, 'blog.html', context)
