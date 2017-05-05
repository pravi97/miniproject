# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-05 20:32
from __future__ import unicode_literals

import administration.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ua', models.CharField(help_text='User agent. We can use this to determine operating system and browser in use.', max_length=2000)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('ip', models.GenericIPAddressField()),
                ('usage', models.CharField(max_length=255)),
                ('login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('value', models.TextField(blank=True)),
                ('file', models.FileField(blank=True, help_text='Some configuration options are for file uploads', null=True, upload_to='configuration')),
                ('help_text', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('file', models.FileField(upload_to='templates', validators=[administration.models.validate_file_extension])),
                ('general_student', models.BooleanField(default=False, help_text='Can be used on student reports')),
                ('report_card', models.BooleanField(default=False, help_text='Can be used on grade reports, gathers data for one year')),
                ('benchmark_report_card', models.BooleanField(default=False, help_text='A highly detailed, single-year report card for benchmark-based grading')),
                ('transcript', models.BooleanField(default=False, help_text='Can be used on grade reports, gathers data for all years')),
            ],
        ),
    ]
