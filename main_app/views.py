from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Dog, Comment

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def dogs_index(request):
    return render(request, 'dogs/index.html', {'dogs': dogs})

# @login_required


def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
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
    return redirect('detail')

# add delete and update comments here


class DogCreate(LoginRequiredMixin, CreateView):
    model = Dog
    fields = ['name', 'breed', 'age',
              'description', 'location', 'date_missing']
    # redirect it to dog detail page later
    success_url = '/dogs/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DogUpdate(LoginRequiredMixin, CreateView):
    model = Dog
    fields = ['description', 'location']


class DogDelete(LoginRequiredMixin, DeleteView):
    model = Dog
    success_url = '/dogs/'
