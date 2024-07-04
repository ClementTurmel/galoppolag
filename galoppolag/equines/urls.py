from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:equine_id>/",        views.equine_detail, name="equine_detail"),
    path("<int:equine_id>/owner/",  views.owner_detail, name="owner_detail"),

    path("lessons/", views.lessons, name="lessons"),
    path("lesson/<int:lesson_id>", views.lesson, name="lesson"),
    path("delete_couple/<int:couple_id>", views.delete_couple, name="delete_couple"),
    path("add_couple/<int:lesson_id>", views.add_couple, name="add_couple"),
]