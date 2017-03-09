from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

import datetime

# Create your models here.
class CrimeRecord(models.Model):
    place = models.CharField(max_length=200)
    incident = models.CharField(max_length=200)
    year = models.IntegerField()
    quarter = models.CharField(max_length=200)
    month = models.IntegerField()
    times = models.IntegerField()

class DisplaySettings(models.Model):
    place = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    quarter = models.CharField(max_length=200)
    month = models.CharField(max_length=200)