# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from treasure.models import *


def leaderboard(request):
    wings = UserProfile.objects.all().order_by('-score')

    index = 1
    for wing in wings:
        wing.rank = index
        wing.save()
        index += 1

    return render(request, 'leaderboard.html', context={'wings': wings})
