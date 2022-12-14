from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# class User(AbstractUser):
#     is_doctor = models.BooleanField('Is doctor', default = False)
#     is_patient = models.BooleanField('Is patient', default = False)

class Vaksin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    name = models.CharField(max_length=100)
    side_effect = models.CharField(max_length=255)
    dose = models.FloatField()
    stock = models.IntegerField()

