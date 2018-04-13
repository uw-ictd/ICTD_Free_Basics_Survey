# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template.loader import get_template
from django.shortcuts import render
from Survey.models import Answers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from Survey.forms import ResultsForm
from django.forms import modelformset_factory

@csrf_protect
def home(request):
    form = ResultsForm()
    return render(request, "home.html", {'form': form})

def results(request):
    if (request.method == 'POST'):
        print("GOT IT!!!")
        res = Answers(q1='e', q2='e', q3='e', q4='e', username="")
        form = ResultsForm(request.POST)
        if (form.is_valid()):
            form.save()
            print("SAVED FORM")
        else:
            print("INVALID FORM")
            # TODO: render error page
    template = get_template("results.html")
    return HttpResponse(template.render());
