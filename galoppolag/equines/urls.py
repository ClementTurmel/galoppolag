from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:equine_id>/",        views.equine_detail, name="equine_detail"),
    path("<int:equine_id>/owner/",  views.owner_detail, name="owner_detail"),
]