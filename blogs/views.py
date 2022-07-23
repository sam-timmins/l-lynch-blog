from django.shortcuts import render

from .models import Blogs


def blogs(request):
    """ A view to return the blogs page """

    blogs = Blogs.objects.all()

    context = {
        'blogs': blogs,
    }

    return render(request, 'blogs/blogs.html', context)
