# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('mascot', 'wing_name', 'score', 'rank', 'solved')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('name', 'correct_answer', 'url', )


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Question, QuestionAdmin)
