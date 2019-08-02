from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from Users.models import Books
from .forms import UserRegisterForm,  UserUpdateForm, ProfileUpdateForm, MyLibraryUpdateForm
from django.shortcuts import render_to_response
from django.db.models import Q



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

@login_required
def mylibrary(request):
    form = MyLibraryUpdateForm()

    if request.method == 'POST':
        form = MyLibraryUpdateForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.user=request.user
            print(form.cleaned_data)
            Books.objects.create(**form.cleaned_data)
            form = MyLibraryUpdateForm()
        else:
            print(form.errors)


    context = {
        'form': form
    }
    return render(request, 'users/MyLibrary.html', context)
