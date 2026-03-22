from django.shortcuts import render
from .models import ProjectPage


    
def project_list(request):
    project_type = request.GET.get("type")

    projects = ProjectPage.objects.live()

    if project_type:
        projects = projects.filter(title__icontains=project_type)

    return render(request, "projects/project_list.html", {
        "projects": projects
    })