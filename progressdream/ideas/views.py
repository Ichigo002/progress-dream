from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.utils import timezone
from .forms import ProjectForm

class ChangePasswordView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('account')
    template_name = 'home/account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        return context

@login_required
def home(request):

    count = []
    for i in range(10):
        count.append(i)

    param = { "count" : count,
              "username" : request.user.username }
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
        form = ProjectForm(request.POST)

        if form.is_valid():
            p = form.save(commit=False)

            p.date_created = timezone.now()
            p.user_id = request.user

            status = form.cleaned_data['status_project']
            p.is_finished = (status == '0')
            p.is_started = (status == '1')
            p.is_cancelled = (status == '2')

            p.save()
            return redirect("home")
        
    else:
        form = ProjectForm()

    param = {'form' : form, 
             "username" : request.user.username}
    
    return render(request, "home/create_project.html", param)
