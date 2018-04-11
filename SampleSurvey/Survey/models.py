# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Assuming we will be encoding answers as a, b, c, or d
class Answers(models.Model):
    q1 = models.CharField(max_length=1)
    q2 = models.CharField(max_length=1)
    q3 = models.CharField(max_length=1)
    q4 = models.CharField(max_length=1)
    RESULTS = (
        ('A', 'Option A'),
        ('B', 'Option B'),
        ('C', 'Option C'),
        ('D', 'Option D'),
    )
    # use .result to get letter encoding, .get_result_display() to get full name
    result = models.CharField(max_length=1, choices=RESULTS)
