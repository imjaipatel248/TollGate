from django.db import models

class updatedb(models.Model):
    vehicle = models.CharField(max_length=100, default='hiiiii')
    amount = models.IntegerField(default=50)