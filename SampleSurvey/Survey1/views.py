# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template.loader import get_template
from django.shortcuts import render
from Survey1.models import basicInfo
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from Survey1.forms import BasicInfoForm

def survey1(request):
    return render(request, "survey1.html", {})

# Rendering the survey page, which will have a results form displayed. See SampleSurvey/templates/home.html
# to see how the form is displayed. To change the display, edit that file. Read more about forms here:
# https://docs.djangoproject.com/en/2.0/topics/forms/modelforms/
@csrf_protect
def basicInfo(request):
    form = BasicInfoForm()
    return render(request, "basicInfo.html", {"form": form})

def results(request):
#    if (request.method == 'POST'):
#    form = ResultsForm(request.POST)
#    if (form.is_valid()):
#        res = form.save()
#        res.result = calculate_result(res)
#        res.save()
#        print("Saved answers with id {0} and username {1}".format(res.id, res.username))
#    else:
#        print("Invalid form, not saved")
    return render(request, "survey1Results.html", {})
