from django import forms
from .models import Student, Course, Qualification

class InsertStudentForm(forms.ModelForm):
    LEVEL_CHOICES = [
        ('IN', 'Initial'),
        ('PR', 'Primary'),
        ('SE', 'Secondary')
    ]

    class Meta:
        model = Student
        fields = ['name', 'surname', 'age', 'grade', 'active', 'level']
        
    def save(self, commit=True):
        student = super().save(commit=False)
        if commit:
            student.save()
        return student

class InsertCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'credits']
        
class QualificationForm(forms.ModelForm):
    course_q = forms.ModelChoiceField(queryset=Course.objects.all(), empty_label="Seleccione un curso")
    student_q = forms.ModelChoiceField(queryset=Student.objects.all(), empty_label="Seleccione un estudiante")

    class Meta:
        model = Qualification
        fields = ['score', 'course_q', 'student_q']