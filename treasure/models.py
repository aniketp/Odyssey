# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    serial = models.IntegerField(null=False, unique=True)
    url = models.IntegerField(max_length=4, null=True)
    name = models.CharField(max_length=30, null=False, blank=False)
    text = models.TextField(max_length=20000, null=True, blank=True)
    points = models.IntegerField(max_length=2, null=True, default=0)
    correct_answer = models.CharField(max_length=100, null=True, blank=True)
    solved_by = models.ManyToManyField(User, related_name='wings', symmetrical=False, blank=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wing_name = models.CharField(max_length=20, unique=True)
    mascot = models.CharField(max_length=30, unique=True)
    score = models.IntegerField(default=0)
    rank = models.IntegerField()
    solved = models.IntegerField(default=0)

    def __str__(self):
        return self.mascot

