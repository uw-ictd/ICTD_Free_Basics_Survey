from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from Survey.models import Answers

class ResultsForm(forms.ModelForm):
    class Meta:
        model = Answers
        fields = ('username',)
