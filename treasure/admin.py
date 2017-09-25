# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('mascot', 'wing_name', 'score', 'rank')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('serial', 'name', 'correct_answer')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
