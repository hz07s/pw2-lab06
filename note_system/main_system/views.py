from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student
from .forms import InsertStudentForm, InsertCourseForm

# Create your views here.
def insertStudent(request):
    form = InsertStudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = InsertStudentForm()

    context = {
        'form': form
        }
    return render(request, 'insertStudent.html', context)

def insertCourse(request):
    form = InsertCourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = InsertCourseForm()

    context = {
        'form': form
        }
    return render(request, 'insertCourse.html', context)
