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
