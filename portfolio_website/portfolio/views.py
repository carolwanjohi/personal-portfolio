from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from .models import Project

# Create your views here.
def index(request):
    '''
    View function for the home page that displays a list project names
    '''
    title = 'Home'
    message = 'Home Page'
    projects = Project.get_projects()
    return render(request,'all-projects/index.html', {"title":title, "message":message, "projects":projects})
