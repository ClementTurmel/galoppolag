from django.contrib import admin

from .models import Equine, Person, LessonParticipant

admin.site.register(Equine)
admin.site.register(Person)
admin.site.register(LessonParticipant)