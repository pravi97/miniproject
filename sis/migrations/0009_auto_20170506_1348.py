# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-06 13:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0008_studentcoursesection'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emergencycontact',
            old_name='pin',
            new_name='zip',
        ),
    ]
