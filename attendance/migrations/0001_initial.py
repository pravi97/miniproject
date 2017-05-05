# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-05 21:57
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schedule', '0006_award_awardstudent_omitcoursegpa_omityeargpa'),
        ('sis', '0007_percoursesectioncohort'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, validators=[django.core.validators.MinValueValidator(datetime.date(1970, 1, 1))])),
                ('asp', models.BooleanField(default=False, help_text='ASP attendance, if unchecked this is for a homeroom')),
                ('course_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.CourseSection')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='"Present" will not be saved but may show as a teacher option.', max_length=255, unique=True)),
                ('code', models.CharField(help_text='Short code used on attendance reports. Ex: A might be the code for the name Absent', max_length=10, unique=True)),
                ('teacher_selectable', models.BooleanField(default=False)),
                ('excused', models.BooleanField(default=False)),
                ('absent', models.BooleanField(default=False, help_text='Some statistics need to add various types of absent statuses, such as the number in parentheses in daily attendance.')),
                ('tardy', models.BooleanField(default=False, help_text='Some statistics need to add various types of tardy statuses, such as the number in parentheses in daily attendance.')),
                ('half', models.BooleanField(default=False, help_text='Half attendance when counting. DO NOT check off absent otherwise it will double count!')),
            ],
            options={
                'verbose_name_plural': 'Attendance Statuses',
            },
        ),
        migrations.CreateModel(
            name='CourseSectionAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now, validators=[django.core.validators.MinValueValidator(datetime.date(1970, 1, 1))])),
                ('time_in', models.TimeField(blank=True, null=True)),
                ('notes', models.CharField(blank=True, max_length=500)),
                ('course_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.CourseSection')),
                ('period', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schedule.Period')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.AttendanceStatus')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sis.Student')),
            ],
        ),
        migrations.CreateModel(
            name='StudentAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now, validators=[django.core.validators.MinValueValidator(datetime.date(1970, 1, 1))])),
                ('time', models.TimeField(blank=True, null=True)),
                ('notes', models.CharField(blank=True, max_length=500)),
                ('private_notes', models.CharField(blank=True, max_length=500)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.AttendanceStatus')),
                ('student', models.ForeignKey(help_text="Start typing a student's first or last name to search", on_delete=django.db.models.deletion.CASCADE, related_name='student_attn', to='sis.Student')),
            ],
            options={
                'permissions': (('take_studentattendance', 'Take own student attendance'),),
                'ordering': ('-date', 'student'),
            },
        ),
        migrations.AlterUniqueTogether(
            name='studentattendance',
            unique_together=set([('student', 'date', 'status')]),
        ),
    ]