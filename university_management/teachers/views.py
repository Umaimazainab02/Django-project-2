from django.shortcuts import render
from .models import AddTeachers
# Create your views here.

def teacher_list(request):
    
    return render(request, "teachers.html")

def all_teachers(request):
    all_teachers = AddTeachers.objects.all()
    return render(request, "all_teachers.html", {"teachers": all_teachers})