from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.core.exceptions import PermissionDenied,ObjectDoesNotExist, ViewDoesNotExist
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Dog, Comment
from .forms import SignUpForm, CommentForm, DogForm, EditForm
import logging
import boto3
import uuid
import os


# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', {
        'dogs': dogs,
        })
        

@login_required
# @permission_required('main_app.view_dog', raise_exception=True)
def dogs_detail(request, dog_id):
    try:
        dog = Dog.objects.get(id=dog_id)
        comment_form = CommentForm()
        return render(request, 'dogs/detail.html', {
            'dog': dog,
            'comment_form': comment_form,
        })
    except ObjectDoesNotExist:
        return render(request, 'exception_handlers/dog_not_found.html', status=404)
    


# @login_required
def add_comment(request, dog_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        form.instance.user = request.user
        form.instance.dog = Dog.objects.get(id=dog_id)
        form.save()
    return redirect('detail', dog_id=dog_id)


@login_required
def delete_comment(request, comment_id, dog_id):
    comment = Comment.objects.get(id=comment_id, dog_id=dog_id)
    # if user != user who made the post. else give unauthorized access message
    if request.method == 'POST':
        comment.delete()
    return redirect('detail', dog_id=dog_id)

class DogCreate(LoginRequiredMixin, CreateView):
    model = Dog
    form_class = DogForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class DogUpdate(LoginRequiredMixin, UpdateView):
    model = Dog
    form_class = EditForm


class DogDelete(LoginRequiredMixin, DeleteView):
    model = Dog
    success_url = '/dogs/'


def signup(request):
    if request.user.is_authenticated:
        return redirect ('home')
    error_message = ''
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = SignUpForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


@login_required
def add_picture(request, dog_id):
    picture_file = request.FILES.get('picture-file', None)
    if picture_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + picture_file.name[picture_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(picture_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Picture.objects.create(url=url, dog_id=dog_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', dog_id=dog_id)
