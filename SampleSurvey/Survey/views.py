# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template.loader import get_template
from django.shortcuts import render
from Survey.models import Answers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from Survey.forms import ResultsForm

def home(request):
    return render(request, "index.html", {});

# Rendering the survey page, which will have a results form displayed. See SampleSurvey/templates/home.html
# to see how the form is displayed. To change the display, edit that file. Read more about forms here:
# https://docs.djangoproject.com/en/2.0/topics/forms/modelforms/
@csrf_protect
def dogSurvey(request):
    form = ResultsForm()
    return render(request, "dogSurvey.html", {'form': form})

# Called when the submit button on the home page is pressed. Renders the results page unless there is an
# issue with the form, in which case it renders an error page (both in SampleSurvey/templates). Most of
# the code involves saving the user's answers in the database for future access. 
def results(request):
    if (request.method == 'POST'):
        form = ResultsForm(request.POST)
        if (form.is_valid()):
            res = form.save()
            res.result = calculate_result(res)
            res.save()
            print("Saved answers with id {0} and username {1}".format(res.id, res.username))
        else:
            print("Invalid form, not saved")
    return render(request, "results.html", {'answers': res })

# Calculates what the result should be, can be changed later for different logic/ answers
def calculate_result(res):
    if (res.q1 == 'a'):
        return 'Husky'
    elif (res.q1 == 'b'):
        return 'Golden Retreiver'
    elif (res.q1 == 'c'):
        return 'Pug'
    else:
        return 'Poodle'

def allResults(request):
    all_results = Answers.objects.all()
    return render(request, "allResults.html", {"all_results": all_results})
