from django.shortcuts import render

from blogs.models import Blogs
from .models import Projects


def projects(request):
    """ A view to return the projects page """

    all_projects = Projects.objects.all()
    blogs = Blogs.objects.all()

    projects_list = []
    project_totals = {}

    for blog in blogs:
        for blog_projects in blog.project.all():

            projects_list.append(blog_projects)

            total = projects_list.count(blog_projects)

            project_totals.update({blog_projects : total})


    projects_count = all_projects.count()

    context = {
        'all_projects': all_projects,
        'projects_count': projects_count,
        'project_totals': project_totals,
        'blogs': blogs,
    }

    return render(request, 'projects/projects.html', context)
