from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Student

# Create your views here.
def index(request):  
    return render(request,'student/index.html',{'students':Student.objects.all()})

def view_student(request,id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))