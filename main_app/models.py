from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class Dog(models.Model):
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    age = models.IntegerField()
    description = models.TextField(max_length=250)
    location = models.CharField(max_length=50)
    date_missing = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog_id': self.id})

    # ordering = ['-date']


class Comment(models.Model):
    content = models.CharField(max_length=300)
    date_created = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)


class Picture(models.Model):
    key_name = models.CharField(max_length=150)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
