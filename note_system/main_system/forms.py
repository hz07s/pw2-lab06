from django import forms
from .models import Student

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
