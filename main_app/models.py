from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
STATUS = (
    ('NOT FOUND', 'Not Found'),
    ('FOUND', 'Found'),
)

class Dog(models.Model):
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    age = models.IntegerField()
    description = models.TextField(max_length=250)
    location = models.CharField(max_length=50)
<<<<<<< HEAD
    date_missing = models.DateField('date missing')
=======
    date_missing = models.DateField()
    date_created = models.DateTimeField(default=timezone.now)
>>>>>>> 5963873 (add date created field to Dog)
    status = models.CharField(
        max_length=10,
        choices = STATUS,
        default = STATUS[0][0]
        )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        return f'{self.get_date_missing_display()} on {self.date}'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog_id': self.id})


class Comment(models.Model):
    content = models.CharField(max_length=300)
    date_created = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)


class Picture(models.Model):
    url = models.CharField(max_length=150)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    def __str__(self):
        return self.url



class State(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name
 
class City(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name

class Location(models.Model):
    state = models.CharField(max_length=70) # (State, on_delete=models.CASCADE),
    city = models.CharField(max_length=70)

    def __str__(self):
        return self
