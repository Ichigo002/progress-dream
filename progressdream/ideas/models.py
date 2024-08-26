from django.db import models as m
from django.contrib.auth.models import User

class Language(m.Model):
    name = m.CharField(max_length=40)
    filename_logo = m.ImageField(upload_to="lang_logos/")
    website_link = m.URLField(max_length=255)

    def __str__(self):
        return self.name


class Technology(m.Model):
    name = m.CharField(max_length=100)
    filename_logo = m.ImageField(upload_to="tech_logos/")
    website_link = m.URLField(max_length=255)

    def __str__(self):
        return self.name


# Create your models here.
class Project(m.Model):
    # id specified automatically by django
    title = m.CharField(max_length=250)
    date_created = m.DateField()
    user_id = m.ForeignKey(User, on_delete=m.CASCADE)
    lang_id = m.ForeignKey(Language, on_delete=m.SET_NULL, null=True, verbose_name="Programming Language")
    tech_id = m.ForeignKey(Technology, on_delete=m.SET_NULL, null=True, verbose_name="Technology")
    date_deadline = m.DateField(verbose_name="Date deadline")
    description = m.TextField()
    is_finished = m.BooleanField()
    is_started = m.BooleanField()
    is_cancelled = m.BooleanField()
    github_link = m.CharField(max_length=250, null=True)

    def __str__(self):
        return self.title
    
class Screenshot(m.Model):
    # id specified automatically by django
    project_id = m.ForeignKey(Project, on_delete=m.CASCADE, related_name="screenshots")
    filename = m.ImageField(upload_to="screenshots/", verbose_name="Screenshot image")

    def __str__(self):
        return self.filename
    
