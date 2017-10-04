# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import *
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


success_message = 'Correct Answer !! Next Question is unlocked.'
failure_message = 'Sorry, Try again..'
already_solved = "You've already solved it"


@login_required
def index(request):
    all_questions = Question.objects.all().order_by('serial')
    wing = UserProfile.objects.get(user=request.user)
    questions_solved = wing.solved
    s = questions_solved + 1
    unlocked_questions = all_questions[:s]

    return render(request, 'index.html', context={'questions': unlocked_questions})


@login_required
def questions(request, pk):
    question = Question.objects.get(url=pk)
    wing = UserProfile.objects.get(user=request.user)
    message = None
    form = QuestionForm()

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            answer = form.cleaned_data['answer']
            solvers = question.solved_by.all()

            if answer.lower() == question.correct_answer:
                if request.user not in solvers:
                    message = success_message
                    question.solved_by.add(request.user)
                    question.save()

                    wing.solved += 1
                    wing.score += question.points
                    wing.save()
                else:
                    message = already_solved

            else:
                message = failure_message

        else:

            return render(request, 'question.html', context={'question': question, 'message': message})

    return render(request, 'question.html', context={'question': question, 'message': message, 'form': form})

