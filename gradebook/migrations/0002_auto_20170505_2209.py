# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-05 22:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gradebook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculationrule',
            name='first_year_effective',
            field=models.ForeignKey(help_text='Rule also applies to subsequent years.', on_delete=django.db.models.deletion.CASCADE, related_name='gradebook_calculationrule_set', to='sis.SchoolYear'),
        ),
    ]
