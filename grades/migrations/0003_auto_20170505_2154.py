# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-05 21:54
from __future__ import unicode_literals

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import grades.models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0006_award_awardstudent_omitcoursegpa_omityeargpa'),
        ('sis', '0007_percoursesectioncohort'),
        ('grades', '0002_auto_20170505_2153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True, validators=[django.core.validators.MinValueValidator(datetime.date(1970, 1, 1))])),
                ('grade', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('override_final', models.BooleanField(default=False, help_text='Override final grade for marking period instead of calculating it.')),
                ('comment', models.CharField(blank=True, max_length=500, validators=[grades.models.grade_comment_length_validator])),
                ('letter_grade', models.CharField(blank=True, choices=[('I', 'Incomplete'), ('P', 'Pass'), ('F', 'Fail'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('HP', 'High Pass'), ('LP', 'Low Pass'), ('M', 'Missing')], help_text='Will override grade.', max_length=10, null=True)),
                ('course_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.CourseSection')),
                ('enrollment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schedule.CourseEnrollment')),
                ('marking_period', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schedule.MarkingPeriod')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sis.Student')),
            ],
            options={
                'permissions': (('change_own_grade', 'Change grades for own class'), ('change_own_final_grade', 'Change final YTD grades for own class')),
            },
        ),
        migrations.CreateModel(
            name='StudentYearGrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cached_credits', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('credits_recalculation_needed', models.BooleanField(default=True)),
                ('cached_grade', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Year average')),
                ('grade_recalculation_needed', models.BooleanField(default=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sis.Student')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sis.SchoolYear')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='studentyeargrade',
            unique_together=set([('student', 'year')]),
        ),
        migrations.AlterUniqueTogether(
            name='grade',
            unique_together=set([('student', 'course_section', 'marking_period')]),
        ),
    ]
