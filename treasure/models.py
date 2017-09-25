# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    serial = models.IntegerField(null=False, unique=True)
    name = models.CharField(max_length=30, null=False, blank=False)
    text = models.TextField(max_length=20000, null=True, blank=True)
    correct_answer = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wing_name = models.CharField(max_length=20, unique=True)
    mascot = models.CharField(max_length=30, unique=True)
    score = models.IntegerField(default=0)
    rank = models.IntegerField()

    def __str__(self):
        return self.mascot


class Answer(models.Model):
    correct_answer = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.correct_answer
