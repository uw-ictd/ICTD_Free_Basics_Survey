from django.conf.urls import url
from . import views
from django.contrib import admin

urlpatterns = [ url(r'^$', views.home, name='home'),
                url(r'^results', views.results, name='results'),
                url(r'^allResults', views.allResults, name='allResults'),
                url(r'^error', views.error, name='error'),
]
