# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treasure', '0017_question_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='bonusquestion',
            name='image',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bonusquestion',
            name='image_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
