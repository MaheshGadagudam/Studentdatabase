from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from course.models import Student
def student_detail(request,pk):
    students=get_object_or_404(Student,pk=pk)
    context={
        'students':students,
    }
    return render(request,'student_detail.html',context)