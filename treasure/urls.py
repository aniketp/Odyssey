from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='odyssey'),
    url(r'^question2', views.question2, name='question2'),
    url(r'^question3', views.question3, name='question3'),
    url(r'^question4', views.question4, name='question4'),
    url(r'^question5', views.question5, name='question5'),
    url(r'^question6', views.question6, name='question6'),
    url(r'^question7', views.question7, name='question7'),
]