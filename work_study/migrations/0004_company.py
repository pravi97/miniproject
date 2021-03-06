# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-05 21:41
from __future__ import unicode_literals

import custom_field.custom_field
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_study', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('alternative_contract_template', models.FileField(blank=True, help_text='Optionally use this odt template instead of a global template for this particular company.', null=True, upload_to='contracts_alt')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'Companies',
            },
            bases=(models.Model, custom_field.custom_field.CustomFieldModel),
        ),
    ]
