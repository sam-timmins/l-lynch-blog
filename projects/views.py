from django.shortcuts import render
from .models import Projects


def projects(request):
    """ A view to return the projects page """

    all_projects = Projects.objects.all()

    context = {
        'all_projects': all_projects,
    }

    return render(request, 'projects/projects.html', context)
