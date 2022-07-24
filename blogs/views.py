from django.shortcuts import render, get_object_or_404

from .models import Blogs, Images


def blogs(request):
    """ A view to return the blogs page """

    blogs = Blogs.objects.all()

    context = {
        'blogs': blogs,
    }

    return render(request, 'blogs/blogs.html', context)


def blog_details(request, blog_slug):
    """ individual blog details """

    blog = get_object_or_404(Blogs, slug=blog_slug)

    image_list = []

    for image in blog.image.all():
        image_list.append(image)

    context = {
        'blog': blog,
        'image_list': image_list,
    }

    return render(request, 'blogs/blog-details.html', context)
