# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template.loader import get_template
from django.shortcuts import render
from Survey1.models import Entry, Data, Question, Question1
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from Survey1.forms import BasicInfoForm, ConfirmationForm, SelectionForm, QuestionForm, Question1Form
from Survey1.questions import AllQuestions
import sys

# These functions are called when the corresponding urls are accessed. The request parameter
# is the Http get or post message and any subsequent parameters are integers corresponding to
# what is listed in the url (see Survey1/urls.py).

# Rendering the survey1 home page
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

# Rendering the start page, which contains directions for how to take the survey.
def start(request, id):
    entry = Entry.objects.get(pk=int(id))
    if (request.method == 'POST'):
        form = BasicInfoForm(request.POST, instance=entry)
        if (form.is_valid()):
            res = form.save()
            print("Saved answers with id {0}".format(res.id,))
        else:
            print("Invalid form, not saved")
    url = "/survey1/question/{0}/{1}/".format(id, sys.maxsize)
    url1 = "/survey1/question1/{0}/{1}/".format(id, sys.maxsize)
    url2 = "/survey1/image/"
    return render(request, "start.html", {"url":url, "url1":url1, "url2":url2})

# Rendering the selection page so the user can choose a response for the previous image
def selection(request, id):
    form = SelectionForm()
    return render(request, "selection.html", {"form": form})

# Rendering an image for the user to respond to
def image(request):
    id = 1 # Use this field when we have a bunch of images
    return render(request, "image.html", {"id":id})

# Rendering a question for the user to respond to
# Note that the userId for a Question model corresponds to the pk of the Entry object in the database
def question(request, prevId, qId):
    if (request.method == 'POST' and int(qId)!=sys.maxsize):
        # Normal case, this is not the first question so we must save the previous question
        prev = Question.objects.get(pk=int(prevId))
        form = QuestionForm(request.POST, instance=prev)
        if (form.is_valid() and prev.word1 != prev.word2):
            res = form.save()
            print("Saved answers with id {0}, userId {1}, and questionId {2}".format(res.id,
                                                                                     res.userId, res.questionId))
        else:
            print("Invalid form, not saved, re-rendering page")
            url = "/survey1/question/{0}/{1}/".format(prevId, qId)
            ques = AllQuestions().getQuestion(int(qId))
            return render(request, "question.html", {"question":ques, "form":form, "url":url})
        if (int(qId) == AllQuestions().numQuestions()):
            # Finished last question, render end page
            return render(request, "survey1Results.html")
        else:
            # render the next question
            next = Question()
            next.userId = prev.userId
            next.questionId = int(qId) + 1
            next.save()
            nextId = next.id
            q = QuestionForm(instance=next)
            url = "/survey1/question/{0}/{1}/".format(nextId, (int(qId) + 1))
            ques = AllQuestions().getQuestion(int(qId) + 1)
            return render(request, "question.html", {"question":ques, "form":q, "url":url})
    else:
        # This is the first question, there are no previous questions to save
        next = Question()
        next.userId = int(prevId)
        next.questionId = 1
        next.save()
        nextId = next.id
        q = QuestionForm(instance=next)
        url = "/survey1/question/{0}/{1}/".format(nextId, 1)
        ques = AllQuestions().getQuestion(1)
        return render(request, "question.html", {"question":ques, "form":q, "url":url})


# Same as question handler, but replacing question with question1 to demonstrate a different form of data entry
def question1(request, prevId, qId):
    if (request.method == 'POST' and int(qId)!=sys.maxsize):
        # Normal case, this is not the first question so we must save the previous question
        prev = Question1.objects.get(pk=int(prevId))
        form = Question1Form(request.POST, instance=prev)
        res = form.save()
        numAnswers = 0 # User should select exactly 2 answers as true
        if prev.A == True:
            numAnswers = numAnswers + 1
        if prev.B == True:
            numAnswers = numAnswers + 1
        if prev.C == True:
            numAnswers = numAnswers + 1
        if (form.is_valid() and numAnswers == 2):
            print("Saved answers with id {0}, userId {1}, and questionId {2}".format(res.id,
                                                                                     res.userId, res.questionId))
        else:
            print("Invalid form, re-rendering page")
            url = "/survey1/question1/{0}/{1}/".format(prevId, qId)
            ques = AllQuestions().getQuestion(int(qId))
            return render(request, "question1.html", {"question":ques, "form":form, "url":url})
        if (int(qId) == AllQuestions().numQuestions()):
            # Finished last question, render end page
            return render(request, "survey1Results.html")
        else:
            # render the next question
            next = Question1()
            next.userId = prev.userId
            next.questionId = int(qId) + 1
            next.save()
            nextId = next.id
            q = Question1Form(instance=next)
            url = "/survey1/question1/{0}/{1}/".format(nextId, (int(qId) + 1))
            ques = AllQuestions().getQuestion(int(qId) + 1)
            return render(request, "question1.html", {"question":ques, "form":q, "url":url})
    else:
        # This is the first question, there are no previous questions to save
        next = Question1()
        next.userId = int(prevId)
        next.questionId = 1
        next.save()
        nextId = next.id
        q = Question1Form(instance=next)
        url = "/survey1/question1/{0}/{1}/".format(nextId, 1)
        ques = AllQuestions().getQuestion(1)
        return render(request, "question1.html", {"question":ques, "form":q, "url":url})
