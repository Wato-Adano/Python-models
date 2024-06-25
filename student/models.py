from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    guardian = models.CharField(max_length=100)
    date_birth = models.DateField()
    email = models.EmailField(unique=True)
    age = models.PositiveSmallIntegerField()
    id_number = models.IntegerField(unique=True)
    code = models.PositiveSmallIntegerField(unique=True)
    gender = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    bio = models.TextField()
    picture = models.ImageField(upload_to='student_pictures/')
    
    
def __str__(self):
    return f"{self.first_name}{self.last_name}"

# Teacher Model


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.PositiveSmallIntegerField()
    id_number = models.IntegerField(unique=True)
    course = models.PositiveSmallIntegerField()
    country = models.CharField(max_length=50)
    profile = models.ImageField(upload_to='teacher_profiles/')
    bio = models.TextField()
    years_of_experience = models.PositiveSmallIntegerField()
    experiences = models.TextField()
    
    def __str__(self):
        return f"{self.first_name}{self.last_name}"
    
# Class Model


class ClassDetail(models.Model):
    class_name = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    trainor = models.CharField(max_length=100)
    students = models.CharField(max_length=100)
    schedule = models.TextField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    semester = models.CharField(max_length=50)

# Course Model


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=100)
    number_of_students = models.IntegerField()
    syllabus = models.CharField(max_length=5000)  # Adjust max_length as needed
    department = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    start_date = models.DateField()
    course_trainor = models.CharField(max_length=100)
    end_date = models.DateField()

    