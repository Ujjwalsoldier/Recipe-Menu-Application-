from django.db import models

# Create your models here.

class Student(models.Model):
    #id = models.Autofield()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField( null=True , blank=True)
    image = models.ImageField()
    file = models.FileField()

    def __str__(self):
        return self.name


class Product(models.Model):
    pass  

class Car(models.Model):   
    car_name = models.CharField(max_length=100) 
    speed = models.IntegerField()

    def __str__(self):
        return self.car_name
