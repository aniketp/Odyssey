from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^1234/', views.leaderboard, name='leaderboard'),
]