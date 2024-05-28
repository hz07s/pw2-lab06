from django.shortcuts import render
from .forms import InsertCourseForm

# Create your views here.
def insertCourse(request):
    form = InsertCourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = InsertCourseForm()
        
    context = {
        'form': form
        }
    return render(request, 'insertCourse.html', context)