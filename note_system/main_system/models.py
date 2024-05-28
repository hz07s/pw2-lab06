from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100, blank=False)
    credits = models.IntegerField(blank=False)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']