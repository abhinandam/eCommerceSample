# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-07 16:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20171007_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='job',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
    ]
