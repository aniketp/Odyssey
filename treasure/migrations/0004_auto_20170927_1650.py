# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 16:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('treasure', '0003_auto_20170927_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='correct_answer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='treasure.Answer'),
        ),
    ]
