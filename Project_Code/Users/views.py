from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
#def home(request):
 # return render(request, 'Users/Register.html')
def register(request):
  form = UserCreationForm()
  return render (request,'Users/Register.html', {'form': form})
