from django.db import models

# Create your models here.

class TecnicalSupportStaff(models.Model):
    FIRST_NAME= models.CharField(max_length=40)
    LAST_NAME = models.CharField(max_length=40) 
    AGE = models.IntegerField(default=0)
    ID = models.IntegerField(default=0)
    ADDRESS = models.CharField(max_length=1000)
    PROFESSION = models.CharField(max_length=200)
    CELL_PHONE = models.IntegerField(default=0)
    PHONE = models.IntegerField(default=0)
    EDUCATION = models.CharField(max_length = 250)
    STORY = models.CharField(max_length=500) 
    PHONE_OS = models.CharField(max_length=500)
    HomeLocationLongitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    HomeLocationLatitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    Q1_ANSWER = models.CharField(max_length=500)

