from django.test import TestCase
from equines.models import Person, Equine


class PersonTestCase(TestCase):

    def test_by_default_they_is_no_Person_persisted(self):
        assert len(Person.objects.all()) == 0


    def test_create_a_person_and_save_it_should_be_retrievable(self):
        person = Person(first_name="John", last_name="Doe", email="a@b.c", phone="0123456789", birthday="1990-01-01")
        assert len(Person.objects.all()) == 0
        person.save()
        assert len(Person.objects.all()) == 1


    def test_person_can_be_retrieved_by_attribute(self):
        person = Person(first_name="John", last_name="Doe", email="a@b.c", phone="0123456789", birthday="1990-01-01")
        person.save()
        
        person_from_db = Person.objects.get(first_name="John")
        assert person_from_db.last_name == "Doe"

    def horse_can_be_retireved_by_attribute(self):
        person = Person(first_name="John", last_name="Doe", email="a@b.c", phone="0123456789", birthday="1990-01-01")
        person.save()
        assert len(person.equines.all()) == 0

        equine = Equine(name="Eclair", birthdate="2010-01-01", owner=person)
        equine.save()
        assert len(person.owner_set.all()) == 1
        assert person.owned_horses.first().name == "Eclair" # owned_horses is the related_name of the ForeignKey in Equine model



class OwnedHorsesNames(TestCase):
    def setUp(self):
        create_person()
    
    def test_get_owned_horses_names_with_one_horse_should_return_horse_name(self):
        person = Person.objects.first()
        Equine.objects.create(name="Eclair", birthdate="2010-01-01", owner=person)

        assert person.get_owned_horses_names() == "Eclair"

    def test_get_owned_horses_names_with_two_horses_should_return_horses_names_separated_by_et(self):
        person = Person.objects.first()
        
        Equine.objects.create(name="Eclair", birthdate="2010-01-01", owner=person)
        Equine.objects.create(name="Tonnerre", birthdate="2011-01-01", owner=person)
        
        assert person.get_owned_horses_names() == "Eclair et Tonnerre"

    def test_get_owned_horses_names_with_three_horses_should_return_horses_names_separated_by_comma_and_et(self):
        person = Person.objects.first()
        
        Equine.objects.create(name="Eclair", birthdate="2010-01-01", owner=person)
        Equine.objects.create(name="Tonnerre", birthdate="2011-01-01", owner=person)
        Equine.objects.create(name="Galopin", birthdate="2012-01-01", owner=person)

        assert person.get_owned_horses_names() == "Eclair, Tonnerre et Galopin"
    
########### tools ##########

def create_person():
    return Person.objects.create(
        first_name="John", 
        last_name="Doe", 
        email="a@b.c", 
        phone="0123456789", 
        birthday="1990-01-01"
    )