from django.db import models
from django.utils import timezone
from datetime import datetime
from datetime import time

class tollgatedb(models.Model):
    vehicleno = models.CharField(max_length=100, default='hiiiii')
    vehiclename = models.CharField(max_length=100, default='BIKE')
    src = models.CharField(max_length=20, default='hello')
    dest = models.CharField(max_length=40, default='keew')
    charge = models.IntegerField(default='h6')
    date = models.DateTimeField(default=datetime.now(), blank=True)
    journy = models.CharField(max_length=50, default='single' )
