from django.shortcuts import render

def hub(request):
    return render(request, "hub.html", {})

def new_project(request):
    return render(request, "creator/new_project.html", {})

def new_language(request):
    return render(request, "creator/new_language.html", {})

def new_tech(request):
    return render(request, "creator/new_tech.html", {})

