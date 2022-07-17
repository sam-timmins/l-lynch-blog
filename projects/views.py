from django.shortcuts import render


def projects(request):
    """ A view to return the projects page """

    return render(request, 'projects/projects.html')
