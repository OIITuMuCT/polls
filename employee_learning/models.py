import datetime
from django.db import models
from django.urls import reverse

class Division(models.Model):
    div_name = models.CharField(max_length=25)
    in_scope = models.BooleanField(
        help_text="If the division is target for the learning program, check this field.")


    def __str__(self):
        return self.div_name


class Employee(models.Model):
    PRIORITIES = [('H', 'High'), ('M', 'Medium'), ('L', 'Low'),]
    name = models.CharField(max_length=25, verbose_name="Employee Name")
    priority = models.CharField(max_length=1, 
                                verbose_name="Learning Priorities", 
                                choices=PRIORITIES, default='M')
    reg_date = models.DateField(default=datetime.date.today, 
                                              verbose_name="Data registration Date")
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class PersonalInfo(models.Model):
    name = models.OneToOneField(Employee, 
            on_delete=models.CASCADE, primary_key=True)
    tel = models.CharField(max_length=15)
    address = models.CharField(max_length=50)


    def __str__(self):
        return self.name #, self.tel, self.address

class LearningCourse(models.Model):
    LEVEL = [('B', 'Basic'), ('I', 'Intermediate'), ('A', 'Advanced'),]
    title = models.CharField(max_length=50, unique=True)
    level = models.CharField(max_length=1, choices=LEVEL)
    employee = models.ManyToManyField(Employee)


    def __str__(self) -> str:
        return self.title