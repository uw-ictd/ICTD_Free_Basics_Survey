# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-13 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1', models.CharField(max_length=1)),
                ('q2', models.CharField(max_length=1)),
                ('q3', models.CharField(max_length=1)),
                ('q4', models.CharField(max_length=1)),
            ],
        ),
    ]