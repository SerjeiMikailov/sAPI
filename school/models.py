from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=35)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=35)
    birth = models.DateField()

    def __str__(self):
        return self.name
    

class Course(models.Model):
    Level = (
        ('B', 'Basic'),
        ('I', 'Intermediate'),
        ('A', 'Advanced')
    )
    code_course = models.CharField(max_length=10)
    description = models.CharField(max_length=200)
    level_course = models.CharField(max_length=10)