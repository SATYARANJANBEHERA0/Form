from django.db import models

# Create your models here.
class Student(models.Model):
    firstname = models.CharField(max_length=100)
    lasttname = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    occupation = models.CharField(max_length=30)
    dob = models.DateField()
    image = models.ImageField()
    gender = models.CharField(max_length=6)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    education = models.CharField(max_length=100)
