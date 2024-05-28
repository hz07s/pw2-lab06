from django import forms
from .models import Course

class InsertCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'credits']