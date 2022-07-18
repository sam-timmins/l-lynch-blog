from django.shortcuts import render

from .models import Projects


def projects(request):
    """ A view to return the projects page """

    all_projects = Projects.objects.all()

    projects_count = all_projects.count()

    context = {
        'all_projects': all_projects,
        'projects_count': projects_count,
    }

    return render(request, 'projects/projects.html', context)
