from django.db import models

class logindb1(models.Model):
    username = models.CharField(max_length=100,default='hiiiii', primary_key='true')
    password = models.CharField(max_length=20,default='hello')
    location= models.CharField(max_length=40,default='keew')
    lane = models.CharField(max_length=50,default='lane1'   )
