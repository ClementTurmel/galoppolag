from django.contrib import admin

from .models import Equine, Person, Couple

admin.site.register(Equine)
admin.site.register(Person)
admin.site.register(Couple)