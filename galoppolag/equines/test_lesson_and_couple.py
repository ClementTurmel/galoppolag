from django.test import TestCase
from equines.models import Person, Equine, Lesson, Couple, Instructor, Rider
from django.core.exceptions import ValidationError



class LessonCoupleTestCase(TestCase):

    def setUp(self):
        Rider.objects.create(
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
    
    
    def test_couple_is_a_rider_and_a_equine_associated_to_a_lesson(self):
        instructor = Instructor.objects.first()
        lesson = Lesson.objects.create(instructor=instructor, datetime="2021-01-01 14:00")

        assert len(Couple.objects.all()) == 0

        Couple.objects.create(
            rider=Rider.objects.first(), 
            equine=Equine.objects.first(), 
            lesson=lesson
        )
     
        lesson_from_db = Lesson.objects.first()
        assert lesson_from_db.couples.first().rider.first_name == "John"
        assert lesson_from_db.couples.first().equine.name == "Eclair"
        assert lesson_from_db.instructor.first_name == "Tony"
    
    
    def test_lesson_are_represented_by_a_instructor_and_a_list_of_couple(self):
        instructor = Instructor.objects.first()

        Lesson.objects.create(instructor=instructor, datetime="2021-01-01 14:00")

        assert len(Lesson.objects.all()) == 1

        lesson_from_db = Lesson.objects.get(datetime="2021-01-01 14:00")
        assert lesson_from_db.instructor == instructor

    def test_a_lesson_cant_have_multiple_couple_with_same_rider(self):
        instructor = Instructor.objects.first()
        lesson = Lesson.objects.create(instructor=instructor, datetime="2021-01-01 14:00")
        rider = Rider.objects.first()
        equine = Equine.objects.first()

        Couple.objects.create(rider=rider, equine=equine, lesson=lesson)

        with self.assertRaises(ValidationError) as e:
            Couple.objects.create(rider=rider, equine=equine, lesson=lesson)
        
        self.assertEqual(e.exception.message, f"Rider {rider.first_name} {rider.last_name} is already in this lesson")
