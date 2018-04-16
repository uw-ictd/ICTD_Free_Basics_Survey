# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Assuming we will be encoding answers as a, b, c, or d
# This class holds the information we need from each user, that is, their answers for the 4
# questions, their results, and their username
class Answers(models.Model):
    ANSWER_CHOICES = ( ('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D'),)
    q1 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='')
    q2 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='')
    q3 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='')
    q4 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='')
    result = models.CharField(max_length=20, default='Golden Retriever')    
    username = models.CharField(max_length=30, default='')
    def __str__(self):
        return self.username
