from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.teacher_list, name="teachers"),
    path("all_teachers/", views.all_teachers, name="all_teachers")
]