from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone


STATUS = (
    ('NOT FOUND', 'Not Found'),
    ('FOUND', 'Found'),
)

class Dog(models.Model):
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    age = models.IntegerField()
    description = models.TextField(max_length=1000)
    location = models.CharField(max_length=50)
    date_missing = models.DateField('date missing')
    date_created = models.DateTimeField(default=timezone.now)

    status = models.CharField(
        max_length=10,
        choices = STATUS,
        default = STATUS[0][0]
        )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

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
