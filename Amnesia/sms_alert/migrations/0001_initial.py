# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-22 13:46
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('intervals', models.IntegerField()),
                ('sleep_time', models.TimeField()),
                ('wake_time', models.TimeField()),
                ('phone_number', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('status', models.TimeField()),
            ],
        ),
    ]