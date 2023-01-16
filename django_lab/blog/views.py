# from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from django_lab.blog.models import Blog


def listing(request):
    context = {
        "blogs": Blog.objects.all(),
    }

    return render(request, "blog/listing.html", context)


def view_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    context = {
        "blog": blog,
    }

    return render(request, "blog/view_blog.html", context)
