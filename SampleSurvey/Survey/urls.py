from django.conf.urls import url
from . import views
from django.contrib import admin

urlpatterns = [ url(r'^$', views.home, name='home'),
                url(r'^results', views.results, name='results'),
]
