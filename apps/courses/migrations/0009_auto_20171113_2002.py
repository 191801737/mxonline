# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-13 20:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_video_learn_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseresource',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间'),
        ),
    ]