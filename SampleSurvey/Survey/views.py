# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template.loader import get_template
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    # We'll prob have to put some database initialization stuff here
    template = get_template("home.html")
    #context = Context({});
    #return HttpResponse(template.render(context));
    return HttpResponse(template.render());
