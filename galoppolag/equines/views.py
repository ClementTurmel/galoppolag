from django.shortcuts import render, get_object_or_404
from equines.models import Person, Lesson
from django.http import HttpResponse, Http404
from django.template import loader


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
