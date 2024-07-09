### DJANGO INITIALIZATION ###
import os, sys
#sys.path.append('C:\DEV\galoppolag\galoppolag')
os.environ['DJANGO_SETTINGS_MODULE'] = 'galoppolag.settings'
import django
django.setup()
#############################
from datetime import datetime
from zoneinfo import ZoneInfo
from datetime import timedelta
from equines.models import Equine, Person, Rider, Lesson, Instructor, Couple


TEST_DATETIME = datetime.now(ZoneInfo("Europe/Paris"))

def test_import_persons():

    Person.objects.all().delete()

    create_persons()

    create_equines_with_owner()

    create_riders()

    create_instructors()

    create_lessons()

    bind_riders_to_lessons()


def bind_riders_to_lessons():
    for lesson in Lesson.objects.all():
        for rider in Rider.objects.all()[:5]:
            Couple.objects.create(
                rider=rider,
                equine=Equine.objects.first(),
                lesson=lesson
            )


def create_lessons():
    for i in range(1, 6):
        Lesson.objects.create(
            instructor=Instructor.objects.first(),
            datetime=TEST_DATETIME + timedelta(days=i)
        )

def create_instructors():
    Instructor.objects.create(first_name="Maria", last_name="Goode", birthday="1980-01-01")
    Instructor.objects.create(first_name="Eva", last_name="Mayer", birthday="1981-02-02")


def create_riders():
    for person in Person.objects.all()[:10]:
        Rider.from_person(Person.objects.get(first_name=person.first_name))


def create_equines_with_owner():
    owner = Person.objects.first()

    equines = [
        {
            "name": "Eclair", 
            "birthdate": "2010-01-01", 
            "owner": Person.objects.get(first_name="Clément"), 
            "picture_url": "https://live.staticflickr.com/4517/38874599871_19d32aa58e_q.jpg"
        },
        {"name": "Tonnerre", "birthdate": "2011-02-02", "owner": owner},
        {"name": "Galopin", "birthdate": "2012-03-03", "owner": owner},
        {"name": "Foudre", "birthdate": "2013-04-04", "owner": owner},
        {"name": "Bolt", "birthdate": "2014-05-05", "owner": owner},
    ]

    for equine in equines:
        Equine.objects.create(**equine)


def create_persons():
    persons = [
        {"first_name": "John", "last_name": "Smith", "email": "john.smith@example.com", "phone": "0123456789", "birthday": "1990-01-01"},
        {"first_name": "Jane", "last_name": "Johnson", "email": "jane.johnson@example.com", "phone": "0123456790", "birthday": "1991-02-02"},
        {"first_name": "Clément", "last_name": "Turmel", "email": "a@b.cd", "phone": "0123456789", "birthday": "1990-01-01", "picture_url": "https://lh3.googleusercontent.com/pw/AP1GczPf4COkluuJyEs_HtJNKbFLl4ASybQTHzMOyO198BMb3Cthy-9r4t8t7U_JXWYpAG6jx-w1GY0hW-7Ro1j8wMXP9BCYPRBcoeSoYfD2kDgUExccgPCBakr5-p3MRvMksY8QbB8IlZIS2SHJC70wq1rUlw=w878-h879-s-no?authuser=0"},
        {"first_name": "Jack", "last_name": "Williams", "email": "jack.williams@example.com", "phone": "0123456791", "birthday": "1992-03-03"},
        {"first_name": "James", "last_name": "Brown", "email": "james.brown@example.com", "phone": "0123456792", "birthday": "1993-04-04"},
        {"first_name": "Julia", "last_name": "Jones", "email": "julia.jones@example.com", "phone": "0123456793", "birthday": "1994-05-05"},
        {"first_name": "Jacob", "last_name": "Miller", "email": "jacob.miller@example.com", "phone": "0123456794", "birthday": "1995-06-06"},
        {"first_name": "Jasmine", "last_name": "Davis", "email": "jasmine.davis@example.com", "phone": "0123456795", "birthday": "1996-07-07"},
        {"first_name": "Joseph", "last_name": "Garcia", "email": "joseph.garcia@example.com", "phone": "0123456796", "birthday": "1997-08-08"},
        {"first_name": "Jennifer", "last_name": "Rodriguez", "email": "jennifer.rodriguez@example.com", "phone": "0123456797", "birthday": "1998-09-09"},
        {"first_name": "Jeffrey", "last_name": "Wilson", "email": "jeffrey.wilson@example.com", "phone": "0123456798", "birthday": "1999-10-10"},
        {"first_name": "Joanna", "last_name": "Martinez", "email": "joanna.martinez@example.com", "phone": "0123456799", "birthday": "2000-11-11"},
        {"first_name": "Jerry", "last_name": "Anderson", "email": "jerry.anderson@example.com", "phone": "0123456710", "birthday": "2001-12-12"},
        {"first_name": "Joyce", "last_name": "Taylor", "email": "joyce.taylor@example.com", "phone": "0123456711", "birthday": "2002-01-13"},
        {"first_name": "Jesse", "last_name": "Thomas", "email": "jesse.thomas@example.com", "phone": "0123456712", "birthday": "2003-02-14"},
        {"first_name": "Janet", "last_name": "Harris", "email": "janet.harris@example.com", "phone": "0123456713", "birthday": "2004-03-15"},
        {"first_name": "Jonah", "last_name": "Martin", "email": "jonah.martin@example.com", "phone": "0123456714", "birthday": "2005-04-16"},
        {"first_name": "Jean", "last_name": "Thompson", "email": "jean.thompson@example.com", "phone": "0123456715", "birthday": "2006-05-17"},
        {"first_name": "Jill", "last_name": "White", "email": "jill.white@example.com", "phone": "0123456716", "birthday": "2007-06-18"},
        {"first_name": "Jeremy", "last_name": "Jackson", "email": "jeremy.jackson@example.com", "phone": "0123456717", "birthday": "2008-07-19"},
        {"first_name": "Jessica", "last_name": "Lopez", "email": "jessica.lopez@example.com", "phone": "0123456718", "birthday": "2009-08-20"},
    ]

    for person in persons:
        Person.objects.create(**person)