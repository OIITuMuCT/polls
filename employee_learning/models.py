from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=25)
    

class Division(models.Model):
    div_name = models.CharField(max_length=25)