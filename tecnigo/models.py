from django.db import models

# Create your models here.


class TecnicalSupportStaff(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField(default=0)
    address = models.CharField(max_length=1000)
    profession = models.CharField(max_length=200)
    cell_phone = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    education = models.CharField(max_length=250)
    story = models.CharField(max_length=500)
    phone_os = models.CharField(max_length=500)
    home_location_longitude = models.DecimalField(
        max_digits=22, decimal_places=16, blank=True, null=True
    )
    home_location_latitude = models.DecimalField(
        max_digits=22, decimal_places=16, blank=True, null=True
    )
    q1_answer = models.CharField(max_length=500)
