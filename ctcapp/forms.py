from django import forms
from . import models


class SurveyModelForm(forms.ModelForm):
    class Meta:
        model = models.Survey
        fields = ('first_name', 'last_name', 'email', 'comment')
