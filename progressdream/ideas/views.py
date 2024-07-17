from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.utils import timezone
from django.db.models import Q
from .forms import *
from .models import *

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

    projects = Project.objects.filter(user_id=request.user.id)

    if request.method == "GET":
        search = request.GET.get('search_input', '')

        tech_filter = request.GET.getlist('technology_filter[]')
        lang_filter = request.GET.get('language_filter[]')

        if search:
            projects = projects.filter(
                Q(title__icontains = search) | # __icontains add contain search
                Q(description__icontains = search))
        
        if tech_filter:
            for t in tech_filter:
                projects = projects.filter(tech_id = t) 

        if lang_filter:
            for t in lang_filter:
                projects = projects.filter(lang_id = t) # __ connects like . different tables

        

    projects = projects.select_related("lang_id").select_related("tech_id")

    langs = Language.objects.all()
    techs = Technology.objects.all()

    param = { 
        "search_"  : search,
        "techs"    : techs,
        "langs"    : langs,
        "projects" : projects,
        "username" : request.user.username 
    }
    return render(request, "home/home.html", param)

def techlang(request):

    if request.method == "POST":
        if request.POST.get("type") == '1':
            techform = TechnologyForm(request.POST, request.FILES)
            print(request.FILES.get('filename_logo'))
            if techform.is_valid():
                name = techform.cleaned_data.get("name")
                filename_logo = techform.cleaned_data.get("filename_logo")
                website_link = techform.cleaned_data.get("website_link")

                obj = Technology.objects.create(
                    name = name,
                    filename_logo = filename_logo,
                    website_link = website_link
                )
                obj.save()

                return redirect("home")
            else:
                langform = LanguageForm()
        else:
            langform = TechnologyForm(request.POST, request.FILES)
            if langform.is_valid():
                langform.save()
                return redirect("home")
            else:
                techform = TechnologyForm()
    else:
        techform = TechnologyForm()
        langform = LanguageForm()

    param = {
        "langform" : langform,
        "techform" : techform,
        "username" : request.user.username
    }

    return render(request, "home/techlang.html", param)

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
