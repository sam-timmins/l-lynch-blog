from multiprocessing import context
from django.shortcuts import render

from blogs.models import Blogs

def index(request):
    """ A view to return the index page """

    blog = Blogs.objects.order_by('date').last()

    context = {
        'blog': blog,
    }

    return render(request, 'home/index.html', context)
