from django.db import models

# Create your models here.
class Student(models.Model):
    LEVEL_CHOICES = [
        ('IN', 'Initial'),
        ('PR', 'Primary'),
        ('SE', 'Secondary')
    ]

    name = models.CharField(max_length=50, blank=False)
    surname = models.CharField(max_length=50, blank=False)
    age = models.IntegerField(blank=False)
    grade = models.IntegerField(blank=False)
    active = models.BooleanField(default=True, blank=False)
    level = models.CharField(max_length=2, choices=LEVEL_CHOICES, blank=False)

    def __str__(self):
        return f'{self.name} ({self.grade})'
    class Meta:
        ordering = ['name']
    
class Course(models.Model):
    title = models.CharField(max_length=100, blank=False)
    credits = models.IntegerField(blank=False)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']