from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        label = {
            'student_no': 'Student Number',
            'First_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'fields_of_study': 'Field of study',
            'gpa': 'GPA',
        }

        widgets = {
            'student_no': forms.NumberInput(attrs={'class': 'form-control'}),
            'First_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'fields_of_study': forms.TextInput(attrs={'class': 'form-control'}),
            'gpa': forms.NumberInput(attrs={'class': 'form-control'}),
        }
