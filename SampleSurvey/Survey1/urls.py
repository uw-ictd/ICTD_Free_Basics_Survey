from django.conf.urls import url
from . import views
from django.contrib import admin

# url patterns for survey1. Urls are listed along with the handler to be called when
# it is accessed, for example, when "survey1/image/" is accessed, the image handler
# in the views.py file in this directory is called. Note that "(\d+)" allows integers
# to be filled in. These fields usually correspond to user ids or question ids and are
# passed into the handlers as parameters
urlpatterns = [ url(r'^$', views.survey1, name='survey1'),
                url(r'basicInfo/', views.basicInfo, name='basicInfo'),
                url(r'confirmation/', views.confirmation, name='confirmation'),
                url(r'image/selection/(\d+)/', views.selection, name='selection'),
                url(r'image/', views.image, name='image'),
                url(r'start/(\d+)/', views.start, name='start'),
                url(r'question/(\d+)/(\d+)/', views.question, name='question'),
                url(r'question1/(\d+)/(\d+)/', views.question1, name='question1'),
]
