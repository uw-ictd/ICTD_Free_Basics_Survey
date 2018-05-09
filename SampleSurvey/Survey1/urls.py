from django.conf.urls import url
from . import views
from django.contrib import admin

urlpatterns = [ url(r'^$', views.survey1, name='survey1'),
                url(r'basicInfo/', views.basicInfo, name='basicInfo'),
                url(r'confirmation/', views.confirmation, name='confirmation'),
                url(r'results/(\d+)/', views.results, name='results'),
                url(r'image/selection/(\d+)/', views.selection, name='selection'),
                url(r'image/', views.image, name='image'),
                url(r'question/(\d+)/(\d+)/', views.question, name='question'),
]
