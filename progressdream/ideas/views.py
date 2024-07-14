from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Project

@login_required
def home(request):
    return render(request, "home.html", {})

def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form" : form})

@login_required
def createProject(request):
    if request.method == "POST":
        form = Project(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = Project()
    return render(request, "create_project.html", {'form' : form})
