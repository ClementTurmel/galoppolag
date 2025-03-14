from django.test import TestCase
from equines.models import Person, Equine, Lesson, LessonParticipant, Instructor, Rider
from django.core.exceptions import ValidationError
from datetime import datetime
from zoneinfo import ZoneInfo

TEST_DATETIME = datetime.now(ZoneInfo("Europe/Paris"))

class LessonParticipantTestCase(TestCase):

    def setUp(self):
        Rider.objects.create(
            first_name="John", 
            last_name="Doe", 
            email="a@b.c", 
            phone="0123456789", 
            birthday=datetime.now()
        )
        
        Instructor.objects.create(
            first_name="Tony", 
            last_name="Doe", 
            email="a@b.c", 
            phone="0123456789", 
            birthday=datetime.now()
        )


        Equine.objects.create(
            name="Eclair", 
            birthdate=datetime.now(), 
            owner=Person.objects.first()
        )
    
    
    def test_participant_is_a_rider_and_a_equine_associated_to_a_lesson(self):
        instructor = Instructor.objects.first()
        lesson = Lesson.objects.create(instructor=instructor, datetime=TEST_DATETIME)

        assert len(LessonParticipant.objects.all()) == 0

        LessonParticipant.objects.create(
            rider=Rider.objects.first(), 
            equine=Equine.objects.first(), 
            lesson=lesson
        )
     
        lesson_from_db = Lesson.objects.first()
        assert lesson_from_db.participants.first().rider.first_name == "John"
        assert lesson_from_db.participants.first().equine.name == "Eclair"
        assert lesson_from_db.instructor.first_name == "Tony"
    
    
    def test_lesson_are_represented_by_a_instructor_and_a_list_of_participants(self):
        instructor = Instructor.objects.first()

        Lesson.objects.create(instructor=instructor, datetime=TEST_DATETIME)

        assert len(Lesson.objects.all()) == 1

        lesson_from_db = Lesson.objects.get(datetime=TEST_DATETIME)
        assert lesson_from_db.instructor == instructor

    def test_a_lesson_cant_have_multiple_participants_with_same_rider(self):
        instructor = Instructor.objects.first()
        lesson = Lesson.objects.create(instructor=instructor, datetime=TEST_DATETIME)
        rider = Rider.objects.first()
        equine = Equine.objects.first()

        LessonParticipant.objects.create(rider=rider, equine=equine, lesson=lesson)

        with self.assertRaises(ValidationError) as e:
            LessonParticipant.objects.create(rider=rider, equine=equine, lesson=lesson)
        
        self.assertEqual(e.exception.message, f"Rider {rider.first_name} {rider.last_name} is already in this lesson")

        self.assertEqual(len(LessonParticipant.objects.all()), 1)
