# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template.loader import get_template
from django.shortcuts import render
from Survey.models import Answers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def home(request):
    #template = get_template("home.html")
    c = {}
    #return HttpResonse(template.render())
    return render(request, "home.html", c)

def results(request):
    template = get_template("results.html")
    #context = Context({});
    #return HttpResponse(template.render(context));
    return HttpResponse(template.render());
