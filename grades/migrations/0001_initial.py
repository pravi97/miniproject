# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-05 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GradeComment',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('comment', models.CharField(max_length=500)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
