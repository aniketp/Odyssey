from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('landing.urls')),
    url(r'^treasurehunt/', include('treasure.urls')),
    url(r'^leaderboard/', include('leaderboard.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]
