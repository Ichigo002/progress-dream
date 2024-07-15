from django import forms
from .models import Project

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