from django.db import models

# Create your models here.

class Student(models.Model):
    student_no=models.PositiveIntegerField()
    First_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField(max_length=100)
    fields_of_study=models.CharField(max_length=100)
    gpa=models.FloatField()

    def __str__(self):
        return f"Student : {self.First_name} {self.last_name}"
        
