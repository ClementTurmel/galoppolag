import os, sys
#sys.path.append('C:\DEV\galoppolag\galoppolag')
os.environ['DJANGO_SETTINGS_MODULE'] = 'galoppolag.settings'
import django
django.setup()
from equines.models import Equine, Person


def test_import_persons():

    Person.objects.all().delete()

    persons = [
        {"first_name": "John", "last_name": "Doe", "email": "john.doe@example.com", "phone": "0123456789", "birthday": "1990-01-01"},
        {"first_name": "Jane", "last_name": "Doe", "email": "jane.doe@example.com", "phone": "0123456790", "birthday": "1991-02-02"},
        {"first_name": "Jack", "last_name": "Doe", "email": "jack.doe@example.com", "phone": "0123456791", "birthday": "1992-03-03"},
        {"first_name": "James", "last_name": "Doe", "email": "james.doe@example.com", "phone": "0123456792", "birthday": "1993-04-04"},
        {"first_name": "Julia", "last_name": "Doe", "email": "julia.doe@example.com", "phone": "0123456793", "birthday": "1994-05-05"},
        {"first_name": "Jacob", "last_name": "Doe", "email": "jacob.doe@example.com", "phone": "0123456794", "birthday": "1995-06-06"},
        {"first_name": "Jasmine", "last_name": "Doe", "email": "jasmine.doe@example.com", "phone": "0123456795", "birthday": "1996-07-07"},
        {"first_name": "Joseph", "last_name": "Doe", "email": "joseph.doe@example.com", "phone": "0123456796", "birthday": "1997-08-08"},
        {"first_name": "Jennifer", "last_name": "Doe", "email": "jennifer.doe@example.com", "phone": "0123456797", "birthday": "1998-09-09"},
        {"first_name": "Jeffrey", "last_name": "Doe", "email": "jeffrey.doe@example.com", "phone": "0123456798", "birthday": "1999-10-10"},
        {"first_name": "Joanna", "last_name": "Doe", "email": "joanna.doe@example.com", "phone": "0123456799", "birthday": "2000-11-11"},
        {"first_name": "Jerry", "last_name": "Doe", "email": "jerry.doe@example.com", "phone": "0123456710", "birthday": "2001-12-12"},
        {"first_name": "Joyce", "last_name": "Doe", "email": "joyce.doe@example.com", "phone": "0123456711", "birthday": "2002-01-13"},
        {"first_name": "Jesse", "last_name": "Doe", "email": "jesse.doe@example.com", "phone": "0123456712", "birthday": "2003-02-14"},
        {"first_name": "Janet", "last_name": "Doe", "email": "janet.doe@example.com", "phone": "0123456713", "birthday": "2004-03-15"},
        {"first_name": "Jonah", "last_name": "Doe", "email": "jonah.doe@example.com", "phone": "0123456714", "birthday": "2005-04-16"},
        {"first_name": "Jean", "last_name": "Doe", "email": "jean.doe@example.com", "phone": "0123456715", "birthday": "2006-05-17"},
        {"first_name": "Jackson", "last_name": "Doe", "email": "jackson.doe@example.com", "phone": "0123456716", "birthday": "2007-06-18"},
        {"first_name": "Jocelyn", "last_name": "Doe", "email": "jocelyn.doe@example.com", "phone": "0123456717", "birthday": "2008-07-19"},
        {"first_name": "Jared", "last_name": "Doe", "email": "jared.doe@example.com", "phone": "0123456718", "birthday": "2009-08-20"},
    ]

    for person in persons:
        Person.objects.create(**person)

    # Assurez-vous d'avoir une instance de Person à qui attribuer les chevaux
    owner = Person.objects.first()

    equines = [
        {"name": "Eclair", "birthdate": "2010-01-01", "owner": owner},
        {"name": "Tonnerre", "birthdate": "2011-02-02", "owner": owner},
        {"name": "Galopin", "birthdate": "2012-03-03", "owner": owner},
        {"name": "Foudre", "birthdate": "2013-04-04", "owner": owner},
        {"name": "Bolt", "birthdate": "2014-05-05", "owner": owner},
    ]

    for equine in equines:
        Equine.objects.create(**equine)