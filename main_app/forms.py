from django.db import models
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Comment


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
