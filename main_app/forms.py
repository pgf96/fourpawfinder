from django.db import models
from django import forms
from django.forms import ModelForm
from django.forms.widgets import DateInput, Select
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Comment, Dog

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.date_joined = timezone.now()
        return user

class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['content']

class DogForm(ModelForm):
    class Meta:
        model = Dog
        fields = ['name', 'breed', 'age', 'description', 'location', 'date_missing', 'status']
        widgets = {'date_missing': DateInput(attrs={'type': 'date'})}
