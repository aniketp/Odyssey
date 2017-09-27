# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render


def index(request):
    questions = Question.objects.all().order_by('serial')
    wing = UserProfile.objects.get(user=request.user)
    questions_solved = wing.solved
    s = questions_solved + 1
    unlocked_questions = questions[:s]

    return render(request, 'index.html', context={'questions': unlocked_questions})


def questions(request, pk):
    question = Question.objects.get(url=pk)

    return render(request, 'question.html', context={'question': question})

