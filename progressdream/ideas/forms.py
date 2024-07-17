from django import forms
from .models import *

class ProjectForm(forms.ModelForm):
    status_project = forms.ChoiceField(
        choices=[(0, 'Finished?'), (1, 'Working on?'), (2, 'Cancelled?')],
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

class TechnologyForm(forms.ModelForm):

    class Meta:
        model = Technology
        fields = [
            'name',
            'filename_logo',
            'website_link',
        ]

class LanguageForm(forms.ModelForm):

    class Meta:
        model = Language
        fields = [
            'name',
            'filename_logo',
            'website_link',
        ]