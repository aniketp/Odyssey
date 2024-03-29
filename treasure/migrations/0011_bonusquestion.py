# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 10:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('treasure', '0010_question_points'),
    ]

    operations = [
        migrations.CreateModel(
            name='BonusQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.IntegerField(unique=True)),
                ('url', models.IntegerField(max_length=4, null=True)),
                ('name', models.CharField(max_length=30)),
                ('text', models.TextField(blank=True, max_length=20000, null=True)),
                ('points', models.IntegerField(default=0, max_length=2, null=True)),
                ('correct_answer', models.CharField(blank=True, max_length=100, null=True)),
                ('released', models.BooleanField(default=False)),
                ('solved_by', models.ManyToManyField(blank=True, related_name='bonus_wings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
