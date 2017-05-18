# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
import datetime

@python_2_unicode_compatible
class Questions(models.Model):
    question_text = models.CharField(max_length=200)
    #pub_date = models.DateTimeField('date published')

    def __str__(self):
        """inbuilt method to return Question text instead of Object"""
        self.question_text
    
    #def was_published_recently(self):
     #   self.pub_date>timezone.now()-datetime.timedelta(days=1)

@python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Questions,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    
    def __str__(self):
        """inbuilt method to return Question text instead of Object"""
        self.choice_text