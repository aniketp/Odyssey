# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treasure', '0009_question_solved_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='points',
            field=models.IntegerField(default=0, max_length=2, null=True),
        ),
    ]
