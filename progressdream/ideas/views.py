from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .models import Project

class ChangePasswordView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('account')
    template_name = 'home/account.html'

@login_required
def home(request):

    count = []
    for i in range(10):
        count.append(i)

    param = { "count" : count }
    return render(request, "home/home.html", param)

@login_required
def delete_account(request):
    user = request.user
    user.delete()
    return redirect("home")

def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("home")
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
