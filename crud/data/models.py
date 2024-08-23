from django.db import models

class student(models.Model):
    studentid = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

# Create your models here.