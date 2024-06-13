from django.db import models

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    birthday = models.DateField("Date of birth")
    picture_url = models.URLField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} {self.email} {self.phone}"
    
    def get_owned_horses_names(self) -> str:
        horses = self.owned_horses.all()
        if len(horses) > 1:
            return ", ".join([equine.name for equine in horses[:len(horses)-1]]) + " et " + horses[len(horses)-1].name
        else:
            return horses[0].name

class Equine(models.Model):
    owner = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="owned_horses")
    name = models.CharField(max_length=100)
    birthdate = models.DateField("Date of birth")
    picture_url = models.URLField(null=True, blank=True)


    def __str__(self) -> str:
        return f"{self.name}, {self.birthdate.year}, appartenant à {self.owner.first_name} {self.owner.last_name}"