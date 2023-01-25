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
        fields = ['username', 'first_name', 'last_name', 'email']

class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['content']

class DogForm(ModelForm):
    class Meta:
        model = Dog
        fields = ['name', 'breed', 'age', 'description', 'location', 'date_missing']
        widgets = {'date_missing': DateInput(attrs={'type': 'date'})}

class EditForm(ModelForm):
    class Meta:
        model = Dog
        fields = ['age', 'description', 'location', 'status']
        widgets = {'date_missing': DateInput(attrs={'type':'date'})}

# class SearchForm(forms.Form):
#     fields = ['query']
#     query = forms.CharField(max_length=100)

