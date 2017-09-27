# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import *
from django.shortcuts import render


success_message = 'Correct Answer !! Next Question is unlocked.'
failure_message = 'Sorry, Try again..'
invalid_form = 'Please Enter Your Answer.'


def index(request):
    all_questions = Question.objects.all().order_by('serial')
    wing = UserProfile.objects.get(user=request.user)
    questions_solved = wing.solved
    s = questions_solved + 1
    unlocked_questions = all_questions[:s]

    return render(request, 'index.html', context={'questions': unlocked_questions})


def questions(request, pk):
    question = Question.objects.get(url=pk)
    wing = UserProfile.objects.get(user=request.user)
    message = None
    form = QuestionForm()

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            answer = form.cleaned_data['answer']

            if answer.lower() == question.correct_answer:
                message = success_message
                wing.solved += 1
                wing.save()

            else:
                message = failure_message

        else:
            message = invalid_form

            return render(request, 'question.html', context={'question': question, 'message': message})

    return render(request, 'question.html', context={'question': question, 'message': message, 'form': form})

