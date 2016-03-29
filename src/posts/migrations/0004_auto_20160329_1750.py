# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-29 17:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20160329_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2016, 3, 29, 17, 50, 37, 27739, tzinfo=utc)),
            preserve_default=False,
        ),
    ]