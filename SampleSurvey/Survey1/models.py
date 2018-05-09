# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Entry(models.Model):
    # For basic info form
    GENDER = ((None, ''), ('F','Female'), ('M','Male'), ('O', 'Other'), )
    YES_NO = ((None,''), ('T','Yes'), ('F', 'No'), )
    EDUCATION = ((None, ''), ('a', 'Pre-High School'), ('b', 'High School'), ('c', 'College'), ('d', 'Graduate School'),
                  ('e', 'Professional School'), ('f', 'PhD'), ('g', 'Postdoctorial'), )
    takenBefore = models.CharField(max_length=3, choices=YES_NO, default='')
    gender = models.CharField(max_length=7, choices=GENDER, default='')
    age = models.PositiveSmallIntegerField(null=True)
    education = models.CharField(max_length=20, choices=EDUCATION, default='')
    glasses = models.CharField(max_length=3, choices=YES_NO, default='')
    personalComputer = models.BooleanField()

    # For confirmation form
    confirmation = models.BooleanField()

class Data(models.Model):
    CHOICES = (('1', '1 - Not colorful at all'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'),
               ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10 - Very colorful'),) 
    answer = models.PositiveSmallIntegerField(choices=CHOICES)
    userId = models.IntegerField()

class Question(models.Model):
    answer = models.CharField(max_length=10, default='')
