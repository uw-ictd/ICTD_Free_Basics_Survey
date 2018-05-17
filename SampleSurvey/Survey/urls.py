from django.conf.urls import url
from . import views
from django.contrib import admin

# urls for the dog survey and the handler function to be called when that url is
# navigated to (ex "dogSurvey/results" is handled by the results function in
# the views.py file in this directory)
urlpatterns = [ url(r'^$', views.home, name='home'),
                url(r'^dogSurvey/$', views.dogSurvey, name='dogSurvey'),
                url(r'^dogSurvey/results', views.results, name='results'),
                url(r'^dogSurvey/allResults', views.allResults, name='allResults'),
]
