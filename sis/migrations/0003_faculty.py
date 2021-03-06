# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-05 17:14
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('sis', '0002_emergencycontact_emergencycontactnumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128)),
                ('ext', models.CharField(blank=True, max_length=10, null=True)),
                ('teacher', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Faculty',
                'ordering': ('last_name', 'first_name'),
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
