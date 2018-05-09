# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template.loader import get_template
from django.shortcuts import render
from Survey1.models import Entry, Data, Question
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from Survey1.forms import BasicInfoForm, ConfirmationForm, SelectionForm, QuestionForm
from Survey1.questions import AllQuestions

def survey1(request):
    return render(request, "survey1.html", {})

# Rendering the confirmation page
@csrf_protect
def confirmation(request):
    form = ConfirmationForm()
    return render(request, "confirmation.html", {"form": form})

# Rendering the bsic info page
@csrf_protect
def basicInfo(request):
    # This method should be called after the confirmation page is submitted
    # Dealing with the results of the confirmation
    if (request.method == 'POST'):
        confForm = ConfirmationForm(request.POST)
        if (confForm.is_valid()):
            res = confForm.save()
            print("Saved answers with id {0}".format(res.id))
        else:
            print("Invalid form, not saved")
    # Rendering this page
    form = BasicInfoForm()
    return render(request, "basicInfo.html", {"form": form, "entry": res,})

def start(request, id):
    entry = Entry.objects.get(pk=int(id))
    if (request.method == 'POST'):
        form = BasicInfoForm(request.POST, instance=entry)
        if (form.is_valid()):
            res = form.save()
            print("Saved answers with id {0}".format(res.id,))
        else:
            print("Invalid form, not saved")
    return render(request, "start.html")

# Not used for survey 1
def selection(request, id):
    form = SelectionForm()
    return render(request, "selection.html", {"form": form})
def image(request):
    id = 1 # Use this field when we have a bunch of images
    return render(request, "image.html", {"id":id})

def question(request, prevId, qId):
    if (request.method == 'POST'): # TODO add check for when this is the first time through
        prev = Question.objects.get(pk=int(prevId))
        form = QuestionForm(request.POST, instance=prev)
        if (form.is_valid()):
            res = form.save()
            print("Saved answers with id {0}".format(res.id,))
        else:
            print("Invalid form, not saved")    
    if (int(qId) == AllQuestions().numQuestions()):
        # Finished last question, render end page
        return render(request, "survey1Results.html")
    next = Question()
    next.save()
    nextId = next.id
    q = QuestionForm(instance=next)
    url = "/survey1/question/{0}/{1}/".format(nextId, (int(qId) + 1))
    ques = AllQuestions().getQuestion(int(qId) + 1)
    return render(request, "question.html", {"question":ques, "form":q, "url":url})
