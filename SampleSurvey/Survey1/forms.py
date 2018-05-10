from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from Survey1.models import Entry, Data, Question

# Specifying which model and which fields I want to display when I use a basicInfo form
class BasicInfoForm(forms.ModelForm):
    age = forms.IntegerField(localize=True, required=True)
#    personalComputer = forms.BooleanField(required=True)
    class Meta:
        model = Entry
        fields = ['takenBefore', 'gender', 'age', 'education', 'glasses', 'personalComputer',] 

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
