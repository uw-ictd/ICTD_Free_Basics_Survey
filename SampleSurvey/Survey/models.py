# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Assuming we will be encoding answers as a, b, c, or d
class Answers(models.Model):
    q1 = models.CharField(max_length=1)
    q2 = models.CharField(max_length=1)
    q3 = models.CharField(max_length=1)
    q4 = models.CharField(max_length=1)
    username = models.CharField(max_length=30)
    def get_result(self):
        if (self.q1 == 'e' or self.q2 == 'e' or self.q3 == 'e' or self.q4 == 'e'):
            return "Please answer all questions"
        if (self.q1 == 'a'):
            return "Golden Retriever"
        elif (self.q1 == 'b'):
            return "Husky"
        elif (self.q1 == 'c'):
            return "Poodle"
        else:
            return "Pug"
    
