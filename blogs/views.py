from django.shortcuts import render


def blogs(request):
    """ A view to return the blogs page """

    context = {

    }

    return render(request, 'blogs/blogs.html', context)
