from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from .models import Project

# Create your views here.
def index(request):
    '''
    View function for the home page that displays a list project names
    '''
    title = 'Home'
    projects = Project.get_projects()
    return render(request,'all-projects/index.html', {"title":title, "projects":projects})

def project(request, project_id):
    '''
    View function that displays a single project and its details
    '''

    # Check if project with the given id exists
    try:
        project = Project.objects.get(id=project_id)
    except DoesNotExist:
        raise Http404()

    title = f'{project.name}'
    return render(request, 'all-projects/project.html', {"title":title, "project":project})

