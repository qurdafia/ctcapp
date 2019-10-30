from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^surveys/', views.surveys, name='surveys'),
    url(r'^survey_form/', views.survey_form, name='survey_form'),
    url(r'^survey/(?P<pk>[0-9]+)/$', views.survey_detail, name='survey'),
]