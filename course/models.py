from django.db import models

class Student(models.Model):
    roll_number=models.CharField(max_length=100)
    student_name=models.CharField(max_length=100)
    father_name=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    address=models.CharField(max_length=150)
    photo=models.ImageField(upload_to='images')

    def __str__(self):
        return self.student_name