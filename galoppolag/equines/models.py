from django.db import models

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

class Equine(models.Model):
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    birthdate = models.DateField("Date of birth")


