from django.db import models

# Create your models here.

class Person(models.Model):
    Name=models.CharField(max_length=100)
    age=models.IntegerField()