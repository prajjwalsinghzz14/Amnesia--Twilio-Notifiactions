# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-25 15:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms_alert', '0004_auto_20180324_1555'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='age',
            new_name='sleeping_hours',
        ),
        migrations.RemoveField(
            model_name='user',
            name='wake_time',
        ),
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.TimeField(blank=True, default=datetime.datetime(2018, 3, 25, 20, 53, 24, 300076)),
        ),
    ]