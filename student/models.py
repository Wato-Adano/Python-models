from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    date_of_birth = models.DateField()
    country = models.CharField(max_length=28)
    Code = models.PositiveSmallIntegerField(max_length=30)
    Gender = models.PositiveSmallIntegerField(max_length=29)
    Age = models.PositiveSmallIntegerField(max_length=27)
    
      
def __str__(self):
    return f"{self.first_name}{self.last_name}"


class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    date_of_birth = models.DateField()
    country = models.CharField(max_length=28)
    Code = models.PositiveSmallIntegerField(max_length=30)
    Gender = models.PositiveSmallIntegerField(max_length=29)
    Age = models.PositiveSmallIntegerField(max_length=27)
    
    def __str__(self):
        return f"{self.first_name}{self.last_name}"
    