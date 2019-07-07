from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
#def home(request):
 # return render(request, 'Users/Register.html')
def register(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        messages.success(request, f'Account created for {username}!')
        return redirect ('Homepage-home')
  else:
    form = UserCreationForm()
  return render (request,'Users/Register.html', {'form': form})
