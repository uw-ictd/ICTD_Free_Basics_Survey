# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Entry(models.Model):
    # For basic info form
    CHOICES = (('', ''), ('1', '1 - Not at all'), ('2','2'), ('3','3'), ('4', '4'), ('5', '5 - very much'), )
    learn = models.CharField(max_length=10, choices=CHOICES, default='')
    fun = models.CharField(max_length=10, choices=CHOICES, default='')
    bored = models.CharField(max_length=10, choices=CHOICES, default='')
    science = models.CharField(max_length=10, choices=CHOICES, default='')
    compare = models.CharField(max_length=10, choices=CHOICES, default='')

    # For confirmation form
    confirmation = models.BooleanField()

class Data(models.Model):
    CHOICES = (('1', '1 - Not colorful at all'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'),
               ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10 - Very colorful'),) 
    answer = models.PositiveSmallIntegerField(choices=CHOICES)
    userId = models.IntegerField()

class Question(models.Model):
    CHOICES = ((None, ''), ('a', 'A'), ('b', 'B'), ('c', 'C'),)
    word1 = models.CharField(max_length=1, default='', choices=CHOICES)
    word2 = models.CharField(max_length=1, default='', choices=CHOICES)
    userId = models.IntegerField()
    questionId = models.IntegerField()
    
