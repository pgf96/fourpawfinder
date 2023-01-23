from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView

from.models import Dog, Comment

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# @login_required
def dogs_index(request):
    # dogs = Dog.objects.filter(user=request.user)
    return render(request, 'dogs/index.html',{'dogs': dogs})

# @login_required
def dogs_detail(request, dog_id):
    comment_form = CommentForm()
    return render(request, 'dogs/detail.html', {
        'dog': dog,
        'comment_form': comment_form,
    })

# @login_required
def add_comment(request, dog_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.dog_id = dog_id
        new_comment.save()
    return redirect('detail', dog_id=dog_id)

# add delete and update comments here

class DogCreate(LoginRequiredMixin, CreateView):
    model = Dog
    fields = ['name', 'breed', 'age', 'description', 'location', 'date_missing']

class DogUpdate(Login)
