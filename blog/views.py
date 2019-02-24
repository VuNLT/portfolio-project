from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blogs(request):
	blogs = Blog.objects
	blog_active = True
	return render(request, 'blog/all_blogs.html', {'blogs':blogs, 'blog_active':blog_active})


def detail(request, blog_id):
	detail_blog = get_object_or_404(Blog, pk=blog_id)
	blog_active = True
	return render(request, 'blog/detail.html', {'blog':detail_blog, 'blog_active':blog_active})