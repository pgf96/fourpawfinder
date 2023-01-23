from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Dog(models.Model):
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    age = models.IntegerField()
    description = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    ordering = ['-date']


class Comment(models.Model):
    content = models.CharField(max_length=300)
    date_created = models.DateField()
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']


class Picture(models.Model):
    key_name = models.CharField(max_length=150)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
