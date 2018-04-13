from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from Survey.models import Answers

# Specifying which model and which fields I want to display when I use a results form
class ResultsForm(forms.ModelForm):
    class Meta:
        model = Answers
        fields = ['username', 'q1', 'q2', 'q3', 'q4',]
