from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from Survey1.models import Entry, Data, Question, Question1

# Specifying which model and which fields I want to display
# These forms convert a model into a format that can be displayed in the site
# for the user to fill in answers

class BasicInfoForm(forms.ModelForm):
    age = forms.IntegerField(localize=True, required=True)
    class Meta:
        model = Entry
        fields = ['learn', 'fun', 'bored', 'science', 'compare', ] 

class ConfirmationForm(forms.ModelForm):
    confirmation = forms.BooleanField(required=True)
    class Meta:
        model = Entry
        fields = ['confirmation',]

class SelectionForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['answer',]

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['word1', 'word2']

class Question1Form(forms.ModelForm):
    class Meta:
        model = Question1
        fields = ['A', 'B', 'C']
