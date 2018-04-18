from django.conf.urls import url
from . import views
from django.contrib import admin

urlpatterns = [ url(r'^$', views.home, name='home'),
                url(r'^dogSurvey/$', views.dogSurvey, name='dogSurvey'),
                url(r'^dogSurvey/results', views.results, name='results'),
                url(r'^dogSurvey/allResults', views.allResults, name='allResults'),
]
