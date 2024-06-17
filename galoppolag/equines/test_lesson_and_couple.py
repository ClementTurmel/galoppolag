from django.test import TestCase
from equines.models import Person, Equine, Lesson, Couple, Instructor



class LessonCoupleTestCase(TestCase):

    def setUp(self):
        Person.objects.create(
            first_name="John", 
            last_name="Doe", 
            email="a@b.c", 
            phone="0123456789", 
            birthday="1990-01-01"
        )
        
        Instructor.objects.create(
            first_name="Tony", 
            last_name="Doe", 
            email="a@b.c", 
            phone="0123456789", 
            birthday="1990-01-01"
        )


        Equine.objects.create(
            name="Eclair", 
            birthdate="2010-01-01", 
            owner=Person.objects.first()
        )
    
    
    def test_couple_is_a_person_and_a_equine_associated_to_a_lesson(self):
        instructor = Instructor.objects.first()
        lesson = Lesson.objects.create(instructor=instructor, datetime="2021-01-01 14:00")

        assert len(Couple.objects.all()) == 0

        Couple.objects.create(
            Person=Person.objects.first(), 
            Equine=Equine.objects.first(), 
            lesson=lesson
        )
     
        couple_from_db = Couple.objects.first()
        assert couple_from_db.Person.first_name == "John"
        assert couple_from_db.Equine.name == "Eclair"
        assert couple_from_db.lesson.instructor.first_name == "Tony"
    
    
    def test_lesson_are_represented_by_a_instructor_and_a_list_of_couple(self):
        instructor = Instructor.objects.first()

        Lesson.objects.create(instructor=instructor, datetime="2021-01-01 14:00")

        assert len(Lesson.objects.all()) == 1

        lesson_from_db = Lesson.objects.get(datetime="2021-01-01 14:00")
        assert lesson_from_db.instructor == instructor