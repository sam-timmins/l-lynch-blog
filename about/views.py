from django.shortcuts import render


def about(request):
    """ A view to return the about page """

    context = {
    }

    return render(request, 'about/about.html', context)
