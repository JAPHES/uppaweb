from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'uppa/home.html')

def about(request):
    return render(request, 'uppa/about us.html')

def departments(request):
    return render(request, 'uppa/departments.html')

def contact(request):
    return render(request, 'uppa/contact us.html')

def team(request):
    return render(request, 'uppa/team.html')

def projects(request):
    return render(request, 'uppa/projects.html')


def health(request):
    """Lightweight health endpoint without touching templates or the database."""
    return HttpResponse("OK", content_type="text/plain")
