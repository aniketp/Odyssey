from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='odyssey'),
    url(r'^question/(?P<pk>\d+)/$', views.questions, name='questions'),
    url(r'^bonus-question/(?P<pk>\d+)/$', views.bonus_questions, name='bonus-questions'),
    url(r'^basu-question1/(?P<pk>\d+)/$', views.basu_question1_2, name='basu-questions1_2')
]