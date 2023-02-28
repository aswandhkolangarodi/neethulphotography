from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request, "web/base.html")

def index(request):
    context = {
        'is_index':True,
    }
    return render(request, "web/index.html",context)

def about(request):
    context = {
        'is_about':True,
    }
    return render(request, "web/about.html",context)

def projects(request):
    context = {
        'is_projects':True,
    }
    return render(request, "web/projects.html",context)

def services(request):
    context = {
        'is_services':True,
    }
    return render(request, "web/services.html",context)