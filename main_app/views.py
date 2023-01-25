from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Dog, Comment, Picture
from .forms import SignUpForm, CommentForm, DogForm
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
    return render(request, 'dogs/index.html', {'dogs': dogs})


@login_required
def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    comment_form = CommentForm()
    return render(request, 'dogs/detail.html', {
        'dog': dog,
        'comment_form': comment_form,
    })


@login_required
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
    fields = ['description', 'location', 'status']


class DogDelete(LoginRequiredMixin, DeleteView):
    model = Dog
    success_url = '/dogs/'


def signup(request):
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


def add_picture(request, dog_id):
    # photo-file will be the "name" attribute on the <input type="file">
    picture_file = request.FILES.get('picture-file', None)
    if picture_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + picture_file.name[picture_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(picture_file, bucket, key)
            # build the full url string
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            Picture.objects.create(url=url, dog_id=dog_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', dog_id=dog_id)





