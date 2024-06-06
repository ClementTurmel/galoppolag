from django.test import TestCase
from equines.models import Equine, Person


class EquineTestCase(TestCase):

    def test_retrieving_equine_using_filter(self):
        person = Person(first_name="John", last_name="Doe", email="a@b.c", phone="0123456789")
        person.save() # person must be saved before equine can be saved 
        equine = Equine(owner=person, name="Ponyta", birthdate="2010-01-01")

        equine.save()

        equines_from_db = Equine.objects.filter(name__startswith="Pony").all()

        assert len(equines_from_db) == 1
        assert equines_from_db[0].name == "Ponyta"

    def test_persisting_equine_without_owner_should_fail(self):
        #Why ? because, by default, owner attribute in models is a 'models.ForeignKey' on person, 
        #witch create a migration with a NOT NULL constraint by default
        equine = Equine(name="Ponyta", birthdate="2010-01-01")

        try:
            equine.save()
        except Exception as e:
            assert str(e) == "NOT NULL constraint failed: equines_equine.owner_id"