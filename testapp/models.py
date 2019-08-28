from django.db import models


# Create your models here.
class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=64)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=64)

class Users(models.Model):
    name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    image_profile = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    telefono = models.CharField(max_length=300)
    rut = models.CharField(max_length=64)
    accepterms = models.BooleanField(default=False)
