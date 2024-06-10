from django.shortcuts import render
from equines.models import Person
from django.http import HttpResponse


def index(request):
    oldest_person = Person.objects.order_by("birthday")[:5]
    output = ", ".join([f"{p.first_name} ({p.birthday.year})" for p in oldest_person])
    return HttpResponse(output)


def equine_detail(request, equine_id):
    return HttpResponse(f"You're looking at equine {equine_id}")

def owner_detail(request, equine_id):
    return HttpResponse("You're looking at owner %s." % equine_id)
