# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# This model recreated the first step in a LabintheWild study: getting confirmation that the user
# agrees to be in the study and gathering information about them. For more information, see
# SampleSurvey/SampleSurvey/templates/basicInfo.html or confirmation.html
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

# This model is used to record a user's evaluation of the colorfulness of a web page that is flashed on
# their screen. See SampleSurvey/SampleSurvey/templates/selection.html
class Data(models.Model):
    CHOICES = (('1', '1 - Not colorful at all'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'),
               ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10 - Very colorful'),) 
    answer = models.PositiveSmallIntegerField(choices=CHOICES)
    userId = models.IntegerField()

# This model is used to record a user's answer to which two of three words are associated. See
# SampleSurvey/SampleSurvey/templates/question.html
class Question(models.Model):
    CHOICES = ((None, ''), ('a', 'A'), ('b', 'B'), ('c', 'C'),)
    word1 = models.CharField(max_length=1, default='', choices=CHOICES)
    word2 = models.CharField(max_length=1, default='', choices=CHOICES)
    userId = models.IntegerField()
    questionId = models.IntegerField()

# This model has the same purpose as Question but demonstrates a different form of data entry.
# See SampleSurvey/SampleSurvey/templates/question1.html
class Question1(models.Model):
    A = models.BooleanField(null=False, default=False)
    B = models.BooleanField(null=False, default=False)
    C = models.BooleanField(null=False, default=False)
    userId = models.IntegerField()
    questionId = models.IntegerField()
    
