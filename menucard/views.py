from django.shortcuts import render
from .models import Project,Banner
# Create your views here.


def index(request,uid):
    project_obj = Project.objects.filter(uid=uid).first()
    banners = Banner.objects.filter(project=project_obj)
    context = {
        "banners":banners,
        "project":project_obj,
    }
    return render(request, 'menucard/index.html',context)