from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

# Create your views here.
def home(requests):
    projects=Project.objects.all()
    return render(requests,'portfolio/home.html',{'projects':projects})
