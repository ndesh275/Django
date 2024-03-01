from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=20)
    phone = models.IntegerField()
    email = models.EmailField(blank=False)
    image = models.ImageField(upload_to='images/', blank=False, default='default.jpg')

    def __str__(self):
        return self.name



class Teacher(models.Model):
    name = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    phone = models.IntegerField()
    email = models.EmailField(blank=False)

    def __str__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    email = models.EmailField(blank=False)

    def __str__(self):
        return self.name

