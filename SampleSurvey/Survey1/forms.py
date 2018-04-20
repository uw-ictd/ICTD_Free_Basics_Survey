from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from Survey1.models import basicInfo

# Specifying which model and which fields I want to display when I use a results form
class BasicInfoForm(forms.ModelForm):
    class Meta:
        model = basicInfo
        fields = '__all__'
