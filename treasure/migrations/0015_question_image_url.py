# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treasure', '0014_auto_20171005_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='image_url',
            field=models.CharField(default=False, max_length=200),
        ),
    ]