from django.db import models

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} {self.email} {self.phone}"

class Equine(models.Model):
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    birthdate = models.DateField("Date of birth")


    def __str__(self) -> str:
        return f"{self.name}, {self.birthdate.year}, appartenant à {self.owner.first_name} {self.owner.last_name}"