from django import forms
from .models import *
from django.forms import inlineformset_factory



class ProjectForm(forms.ModelForm):
    status_project = forms.ChoiceField(
        choices=[(0, 'Finished?'), (1, 'Working on?'), (2, 'Cancelled?'), (3, 'Not even started')],
        widget=forms.RadioSelect,
    )

    class Meta:
        model = Project
        fields = [
            'title', 
            'tech_id', 
            'lang_id',
            'date_deadline', 
            'description', 
            'github_link'
        ]

class ScreenshotForm(forms.ModelForm):
    class Meta:
        model = Screenshot
        fields = ['filename',]

ScreenshotFormSet = inlineformset_factory(Project, Screenshot, form=ScreenshotForm, extra=1)

class TechnologyForm(forms.ModelForm):

    class Meta:
        model = Technology
        fields = [
            'name',
            'website_link',
        ]

class LanguageForm(forms.ModelForm):

    class Meta:
        model = Language
        fields = [
            'name',
            'website_link',
        ]