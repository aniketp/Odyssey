# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 11:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treasure', '0012_auto_20171005_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='rank',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
