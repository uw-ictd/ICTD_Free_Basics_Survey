# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template.loader import get_template
from django.shortcuts import render
from Survey1.models import Entry, Data
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from Survey1.forms import BasicInfoForm, ConfirmationForm, SelectionForm

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

def results(request, id):
    # Should be called after basicInfo. Adding info to database
    entry = Entry.objects.get(pk=int(id))
    if (request.method == 'POST'):
        form = BasicInfoForm(request.POST, instance=entry)
        if (form.is_valid()):
            res = form.save()
            print("Saved answers with id {0}".format(res.id,))
        else:
            print("Invalid form, not saved")
    entries = Entry.objects.all()
    return render(request, "survey1Results.html", {'entries': entries})

def selection(request):
    form = SelectionForm()
    return render(request, "selection.html", {"form": form})
