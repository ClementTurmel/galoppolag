from django.shortcuts import render, get_object_or_404
from equines.models import Person, Lesson, LessonParticipant, Rider, Equine
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.contrib import messages


def index(request):
    oldest_persons = Person.objects.order_by("birthday")[:5]
    template = loader.get_template("equines/index.html")
    context = {
        "oldest_persons": oldest_persons,
    }
    return render(request, "equines/index.html", context)


def equine_detail(request, equine_id):
    return HttpResponse(f"You're looking at equine {equine_id}")

def owner_detail(request, equine_id):
    person = get_object_or_404(Person, pk=equine_id)
    return render(request, "equines/person.html", {"person": person})


def lessons(request):
    lessons = Lesson.objects.all()
    return render(request, "equines/lessons.html", {"lessons": lessons})

def lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    riders = Rider.objects.all()
    equines = Equine.objects.all()

    context = {
        "lesson": lesson, 
        "riders": riders, 
        "equines": equines
    }

    return render(request, "equines/lesson.html", context)

def delete_participant(request, participant_id):
    participant = get_object_or_404(LessonParticipant, pk=participant_id)
    participant.delete()
    return HttpResponseRedirect(reverse("lesson", args=(participant.lesson.id,)))

def add_participant(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    rider_id = request.POST["rider"]
    equine_id = request.POST["equine"]
    try:
        LessonParticipant.objects.create(
            rider=Rider.objects.get(pk=rider_id),
            equine=Equine.objects.get(pk=equine_id),
            lesson=lesson
        )
    except ValidationError as e:
        messages.error(request, e.message)
    
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse("lesson", args=(lesson_id,)))