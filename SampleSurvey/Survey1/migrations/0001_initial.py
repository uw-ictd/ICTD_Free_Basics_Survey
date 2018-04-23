# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-23 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('takenBefore', models.NullBooleanField(choices=[(None, ''), (True, 'Yes'), (False, 'No')], default=None, max_length=3)),
                ('gender', models.CharField(choices=[(None, ''), ('F', 'Female'), ('M', 'Male'), ('O', 'Other')], default='', max_length=7)),
                ('age', models.PositiveSmallIntegerField()),
                ('education', models.CharField(choices=[(None, ''), ('a', 'Pre-High School'), ('b', 'High School'), ('c', 'College'), ('d', 'Graduate School'), ('e', 'Professional School'), ('f', 'PhD'), ('g', 'Postdoctorial')], default='', max_length=20)),
                ('glasses', models.NullBooleanField(choices=[(None, ''), (True, 'Yes'), (False, 'No')], default=None, max_length=3)),
                ('personalComputer', models.BooleanField()),
                ('confirmation', models.BooleanField()),
            ],
        ),
    ]