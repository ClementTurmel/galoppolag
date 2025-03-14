from django.db import models
from django.core.exceptions import ValidationError
from django.utils import formats

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
        if len(horses) == 0:
            return ""
        if len(horses) > 1:
            return ", ".join([equine.name for equine in horses[:len(horses)-1]]) + " et " + horses[len(horses)-1].name
        else:
            return horses[0].name


class Instructor(Person):
    pass

class Rider(Person):
    pass

    @classmethod
    def from_person(cls, person, **extra_fields):
        rider = cls(person_ptr=person, **extra_fields)
        rider.__dict__.update(person.__dict__)
        rider.save()
        return rider


class Equine(models.Model):
    owner = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="owned_horses")
    name = models.CharField(max_length=100)
    birthdate = models.DateField("Date of birth")
    picture_url = models.URLField(null=True, blank=True)


    def __str__(self) -> str:
        return f"{self.name}, {self.birthdate.year}, appartenant à {self.owner.first_name} {self.owner.last_name}"
    

class Lesson(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name="lessons")
    datetime = models.DateTimeField()


class LessonParticipant(models.Model):
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
    equine = models.ForeignKey(Equine, on_delete=models.SET_NULL, null=True, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="participants")

    def __str__(self) -> str:
        return f"{self.rider.first_name} {self.rider.last_name} " \
            f"et {self.equine.name} "\
            f"dans le cours du {formats.date_format(self.lesson.datetime, 'l d F à H:i')} "\
            f"avec {self.lesson.instructor.first_name} {self.lesson.instructor.last_name}"

    def clean(self):
        lesson_riders = [participant.rider for participant in self.lesson.participants.all()]
        if self.rider in lesson_riders:
            raise ValidationError(f"Rider {self.rider.first_name} {self.rider.last_name} is already in this lesson")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
