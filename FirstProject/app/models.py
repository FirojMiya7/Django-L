from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=50)


class Course(models.Model):
    image=models.ImageField(upload_to="images")
    title=models.CharField(max_length=100)
    description=models.TextField()
    price=models.FloatField()


class Customer(models.Model):
    FirstName=models.CharField(max_length=30)
    LastName=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    confirmPassword=models.CharField(max_length=20)
    comments=models.TextField()
