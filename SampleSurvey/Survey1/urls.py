from django.conf.urls import url
from . import views
from django.contrib import admin

urlpatterns = [ url(r'^$', views.survey1, name='survey1'),
                url(r'basicInfo/', views.basicInfo, name='basicInfo'),
]
