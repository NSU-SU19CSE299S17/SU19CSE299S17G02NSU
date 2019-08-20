from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import MyLibraryList
from .forms import UserRegisterForm,  UserUpdateForm, ProfileUpdateForm, MyLibraryUpdateForm


def register(request):
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'Your Account has been created! You Can Now Login')
        return redirect('login')
  else:
    form = UserRegisterForm()
  return render(request,'Users/Register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

#following function takes user input and adds their books to the table
@login_required
def mylibrary(request):
    if request.method == 'POST':
        Name = request.POST['name']
        Author = request.POST['author']
        Genre = request.POST['genre']
        current_user = request.user

        if request.user.is_authenticated:
            f1 = MyLibraryList.objects.create(UserID=current_user, name=Name, author=Author, genre=Genre)
            temp = MyLibraryList.objects.filter(UserID=request.user)
            context = {
                'c' : f1,
                'obj': temp,
               }
            return render(request, 'Users/mylibrary.html', context)
        else:
            raise Exception('User doesnt exist')
            return render(request, 'Users/mylibrary.html')

    else:
        temp = MyLibraryList.objects.filter(UserID=request.user)
        context = {
            'obj': temp,
        }

        return render(request, 'Users/mylibrary.html', context)
