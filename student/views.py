from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Student
from .forms import StudentForm

# Create your views here.
def index(request):  
    return render(request,'student/index.html',{'students':Student.objects.all()})

def view_student(request,id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            new_student_no=form.cleaned_data['student_no']
            new_First_name=form.cleaned_data['First_name']
            new_last_name=form.cleaned_data['last_name']
            new_email=form.cleaned_data['email']
            new_fields_of_study=form.cleaned_data['fields_of_study']
            new_gpa=form.cleaned_data['gpa']

            new_student=Student(
            student_no=new_student_no,
            First_name=new_First_name,
            last_name=new_last_name,
            email=new_email,
            fields_of_study=new_fields_of_study,
            gpa=new_gpa,
            )
            new_student.save()
            return render(request,'student/add.html',{'form':StudentForm(),'success':True})
    else:
        form=StudentForm()
        return render(request,'student/add.html',{'form':StudentForm()})