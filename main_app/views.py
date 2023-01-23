from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Dog, Comment
from .forms import SignUpForm, CommentForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def dogs_index(request):
    dogs = Dog.objects.all()
<<<<<<< HEAD
    return render(request, 'dogs/index.html', {'dogs': dogs})
=======
    return render(request, 'dogs/index.html',{'dogs': dogs})
>>>>>>> 7b4d3b9 (touch up views)


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
    fields = ['name', 'breed', 'age',
              'description', 'location', 'date_missing']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DogUpdate(LoginRequiredMixin, UpdateView):
    model = Dog
    fields = ['description', 'location']


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




