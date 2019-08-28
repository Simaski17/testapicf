from django.db import models


# Create your models here.
class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=64)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=64)

class Users(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    last_name = models.CharField(max_length=64, blank=True, null=True)
    username = models.CharField(max_length=64, blank=True, null=True)
    password = models.CharField(max_length=64, blank=True, null=True)
    image_profile = models.CharField(max_length=300, blank=True, null=True)
    email = models.CharField(max_length=300, blank=True, null=True)
    telefono = models.CharField(max_length=300, blank=True, null=True)
    rut = models.CharField(max_length=64, blank=True, null=True)
    accepterms = models.BooleanField(default=False)
