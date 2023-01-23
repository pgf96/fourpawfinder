from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Dog(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    breed = models.CharField(max_length=20)
    description = models.CharField(max_length=300)
    location = models.CharField(50)
    date_missing = models.DateField()
    date_missing = models.DateField()

    def __str__(self):
        return self.name


# class Picture(models.Model):
#     url = models.CharField(max_length=200)
#     dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
