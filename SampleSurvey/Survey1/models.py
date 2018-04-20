# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class basicInfo(models.Model):
    GENDER = ((None, ''), ('F','Female'), ('M','Male'), ('O', 'Other'), )
    YES_NO = ((None,''), (True,'Yes'), (False, 'No'), )
    EDUCATION = ((None, ''), ('a', 'Pre-High School'), ('b', 'High School'), ('c', 'College'), ('d', 'Graduate School'),
                  ('e', 'Professional School'), ('f', 'PhD'), ('g', 'Postdoctorial'), )
    takenBefore = models.NullBooleanField(max_length=3, choices=YES_NO, blank=None, null=None, default=None)
    gender = models.CharField(max_length=7, choices=GENDER, default='')
    age = models.PositiveSmallIntegerField()
    education = models.CharField(max_length=20, choices=EDUCATION, default='')
    glasses = models.NullBooleanField(max_length=3, choices=YES_NO, blank=None, null=None, default=None)
    personalComputer = models.BooleanField()
