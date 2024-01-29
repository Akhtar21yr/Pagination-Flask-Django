from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Student(models.Model):
    rollno = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 50,null = False)
    age = models.IntegerField(validators=[MinValueValidator(18)])
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    